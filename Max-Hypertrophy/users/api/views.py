from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework import viewsets
from .models import User 
from .serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet):

    
    serializer_class = UserSerializer

    #-------- Funcion interna para buscar usuarios --------
    def get_queryset(self, queryset):
        username = self.request.GET.get('user')
        if username: 
            return User.objects.filter(username = username).filter(is_active = True)

        return queryset 
               

    # ------- FUNCIONES DE PETICIONES HTTP -----

    def list(self, request):
        """
        El parametro de busquedad del usuario se envia por medio de la URL de la
        siguente manera "xxx/users/?user=username del usuario". 

        Lista todos los usuarios y busca un usuario en concreto si se le 
        envia el username como parametro

              
        """
        
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
                  

    def create(self, request):

        """
        Crea un usuario y lo registra en la base de datos.

        """
         
        if request.method == "POST":
            user_serializer = UserSerializer(data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({"Mensaje":"User Create successfully"},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({"Mensaje":"Error Create User"},
                                status=status.HTTP_401_UNAUTHORIZED)


    def update(self, request):
        """
        Actualiza el usuario que se le envie por parametro y con los nuevos
        datos que se le envie en la el cuerpo de la peticion por medio de un 
        formato JSON. Los datos obligatorios para la actualizacion son 
        'username' y 'email' mas el dato a actualizar si este no son los antes
        mencionados.

        El parametro de busquedad del usuario se envia por medio de la URL de la
        siguente manera "xxx/users/?user=username del usuario".
        """
        if request.method == "PUT":
            user = self.get_queryset(request)
            user_serializer = UserSerializer(user, data = request.data) 
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'Message':'User successfully update'}, 
                                status=status.HTTP_202_ACCEPTED)
            
            return Response(user_serializer.errors)
        
    def destroy(self, request):
        """
        
        El parametro de busquedad del usuario se envia por medio de la URL de la
        siguente manera "xxx/users/?user=username del usuario".

        Elimina de manera logica al usuario que se le envie por parametro
        cambiando su estado 'is_active' de True a False. 

        """

        if request.method == "DELETE":
            user = self.get_queryset(request)
            user.is_active = False
            user.save()
            return Response({'Message':'User successfully deleted'}, 
                            status=status.HTTP_200_OK)

    

