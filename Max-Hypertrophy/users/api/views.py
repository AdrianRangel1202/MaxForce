from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import  status
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def UsersViews(request):
    
    if request.method == "GET":
        users = User.objects.all()
        srlz = UserSerializer(users, many=True)
        return Response(srlz.data)

    if request.method == "POST":
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"Mensaje":"User Create successfully"}, status=status.HTTP_201_CREATED)
        else:
             return Response({"Mensaje":"Error Create User"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(["GET","PUT", "DELETE"])
def filter_user(request, pk = None): 

    if request.method == "GET":
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user, data = request.data) 
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'Message':'User successfully update'}, status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors)

    if request.method == "DELETE":
        user = User.objects.filter(id = pk).first()
        user.delete()
        return Response({'Message':'User successfully deleted'}, status=status.HTTP_200_OK)
   

