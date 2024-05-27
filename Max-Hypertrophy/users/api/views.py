from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework.decorators import api_view



#-------- Funcion interna para buscar usuarios --------
def search_user(request):

    '''
    retorna todos los usuarios si no se le envia un username por parametro
    '''

    return UserSerializer.Meta.model.objects.filter(is_active = True) 
    

    
def filter_user(request):  

    '''
    retorna busca el usuario por el username enviado por parametro y retorna solo el primero de la lista
    URL: /user/?username = username del usuario
    '''

    username = request.GET.get('username')
    user = UserSerializer.Meta.model.objects.filter(username = username).filter(is_active = True).first()
    return user 



# ---------- Funciones de View con Api_View Decorators ------ 

@api_view(["GET", "POST"])
def UsersViews(request):
    
    '''
    Retorna todos los usuarios con los parametro : 
    
    {
    "username": "xxxxxx",
    "email": "xxxxxxx",
    "name": "xxxxxx",
    "last_name": "xxxxx"
    },
    
    '''

    if request.method == "GET":
        users = search_user(request)
        srlz = UserSerializer(users, many=True)
        return Response(srlz.data)
    
    '''
    Inserta usuarios en la base de datos solicitando:
    {
        'username':
        'email':
        'password':
    }
    
    Como campos obligatorios
    '''

    if request.method == "POST":
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"Mensaje":"User Create successfully"}, status=status.HTTP_201_CREATED)
        else:
             return Response({"Mensaje":"Error Create User"}, status=status.HTTP_401_UNAUTHORIZED)
        



    
@api_view(["GET","PUT", "DELETE"])
def update_user(request): 

    if request.method == "GET":
        user = filter_user(request)
        if user == None:
            return Response({'message':'User No Exist'}, status=status.HTTP_404_NOT_FOUND)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        user = filter_user(request)
        user_serializer = UserSerializer(user, data = request.data) 
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'Message':'User successfully update'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors)

    if request.method == "DELETE":
        user = filter_user(request)
        user.is_active = False
        user.save()
        return Response({'Message':'User successfully deleted'}, status=status.HTTP_200_OK)
   

