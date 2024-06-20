from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework import viewsets
from .models import User 


class UserViewSets(viewsets.ModelViewSet):

    
    serializer_class = UserSerializer

    #-------- Funcion interna para buscar usuarios --------
    def get_queryset(self, queryset):
        username = self.request.GET.get('user')
        if username: 
            return User.objects.filter(username = username).filter(is_active = True)

        return queryset 
               

    # ------- FUNCIONES DE PETICIONES HTTP -----

    # Muestra todos los usuarios 
    def list(self, request):
        
        if request.method == "GET":
            queryset = User.objects.filter(is_active = True)
            user = self.get_queryset(queryset)
            if user:
                serializer_users = UserSerializer(user, many=True)
                return Response(serializer_users.data, status=status.HTTP_200_OK)
            
            if not user:
                return Response({'Error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)

            else:
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
                  

    #Inserta usuarios en la base de datos solicitando:    
    def create(self, request):
         
        if request.method == "POST":
            user_serializer = UserSerializer(data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"Mensaje":"User Create successfully"},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({"Mensaje":"Error Create User"},
                                status=status.HTTP_401_UNAUTHORIZED)


    # Actualiza un usuario en especifico
    def update(self, request):
        if request.method == "PUT":
            user = self.get_queryset(request)
            user_serializer = UserSerializer(user, data = request.data) 
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'Message':'User successfully update'}, 
                                status=status.HTTP_202_ACCEPTED)
            
            return Response(user_serializer.errors)
        
    # Elimina un usuario 
    def destroy(self, request):

        if request.method == "DELETE":
            user = self.get_queryset(request)
            user.is_active = False
            user.save()
            return Response({'Message':'User successfully deleted'}, 
                            status=status.HTTP_200_OK)

    

