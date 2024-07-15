
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests



class Login(APIView):

        def post(self, request):
                username=request.data.get('username')

                url_user= "localhost/users/?user=" + username
                user= requests.get(url_user)

                if user == 200:
                        url_auth = "localhost/auth/"
                        token = requests.post(url_auth, data={
                                "username":user["username"],
                        })
                        
                        if token == 200:
                                return Response(token['access'], status=status.HTTP_202_ACCEPTED)
                        else:
                                return Response({'Error':"User Not Authentication"}, status=status.HTTP_401_UNAUTHORIZED)


