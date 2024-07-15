from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

class AuthenticationUSer(APIView):

    def post(self, request):
        username= request.data.get('username')

        refresh = RefreshToken.for_user(username)
        return Response(refresh, status=status.HTTP_200_OK)

