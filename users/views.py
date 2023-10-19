from django.shortcuts import render

from users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        data = request.data

        user = get_object_or_404(User, username=data.get("username"))

        if user.check_password(data.get("password")):
            token, created = Token.objects.get_or_create(user = user)
            return Response(data={
                "user":UserSerializer(user).data,
                "token":token.key
            },
            status=status.HTTP_200_OK
            
            )
        else:
            return Response(data={
                "message":"User password is not correct"
            },
            status= status.HTTP_400_BAD_REQUEST
            )
        

class RegisterationView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = data.get("username"))
            user.set_password(data.get("password"))
            user.save()


            ##CREATE TOKEN
            token = Token.objects.create(user = user )


            ##SEND RESPONSE
            return Response(data={
                "user":serializer.data,
                "token":token.key
            },
            status=status.HTTP_201_CREATED
            )
        return Response(data={
            "message":"User was not created"
        },
        status=status.HTTP_400_BAD_REQUEST
        )



class TestView(APIView):
    permission_classes = [ IsAuthenticated ]
    def post(self, request):
        return Response(data={
            "message":f"Logged in as user with this email {request.user.email}"
        },
        status=status.HTTP_200_OK
        )