from django.shortcuts import render
from django.shortcuts import render
from .serializer import *
from rest_framework import status
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from django.http.response import (HttpResponse, HttpResponseNotFound,
                                  HttpResponsePermanentRedirect,
                                  HttpResponseRedirect)

from .models import * 
from django.contrib.auth import authenticate
from .service import *
@api_view(['POST'])
def Register(request):
    #request.data--- dictionary
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        if user:
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])   
def Login(request):
    serializer=LoginSerializer(data=request.data)
    if serializer.is_valid():
        user=B2CUser.objects.get(email=serializer.data["email"])
        user_auth=authenticate(email=user.email,password=serializer.data["password"])
        
        if user_auth:
            token=generate_token(user_auth)
            return Response(token,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['POST'])   
def change_password(request):
    serializer=ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        user=B2CUser.objects.get(email=serializer.data["email"])
        user.set_password(serializer.data["email"])
        user.save() 
        return Response("Password Changed Successfully",status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) 
def AllUserData(request):
    userdata=B2CUser.objects.all()
    serializer=B2CUSerSerializer(userdata,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
    