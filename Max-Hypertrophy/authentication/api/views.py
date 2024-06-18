from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated




class UserAuthJWT(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)


    def authenticate(self, request):
        user = request

        return Response({"message":"Authenticated user"}, status=status.HTTP_202_ACCEPTED)