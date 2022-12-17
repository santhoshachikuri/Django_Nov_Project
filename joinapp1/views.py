from django.shortcuts import render
from joinapp1.serializer import *
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

@api_view(['POST'])
def RollerTableView(request):
    mydata=request.data
    print("my data:",mydata)
    serializer=RollerSerializer(data=mydata)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    



