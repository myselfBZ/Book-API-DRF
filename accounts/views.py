from rest_framework.decorators import api_view
from rest_framework.response import Response 
from API.models import CustomUser
from rest_framework import status 
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
@api_view(["POST"])
def sign_up(request):
    sreialized = UserSerializer(data=request.data)
    if sreialized.is_valid():
        sreialized.save()
        user = User.objects.get(username=request.data['username'])
        custom_user = CustomUser.objects.create(user=user)
        token = Token.objects.create(user=user)
        user.set_password(request.data['password'])
        user.save()
        return Response({"user":sreialized.data, "token":token.key})
    return Response({"message":sreialized.errors})
@api_view(["POST"])
def log_in(request):
    user = get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response({"message":"wrong pass"})
    serializer = UserSerializer(instance=user)
    token, created = Token.objects.get_or_create(user=user)
    return Response({"message":token.key, "data":serializer.data})

@api_view(["GET"])
def token_test(request):
    return Response({})    
