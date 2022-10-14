from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *

# Create your views here.


class Organizations(APIView):
    def get(self,request):
        datas = organization.objects.all()
        serializer = organization_Serializer(datas,many = True).data
        return Response(serializer,status=status.HTTP_200_OK)


    def post(self,request):
        serializer = organization_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class organization_list(APIView):
    def get(self,request,pk):
        try:
            print(pk, organization.objects.get(id = pk),"----------------------------------")
            datas = organization.objects.get(id = pk)
            serializer = organization_Serializer(datas,many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except organization.DoesNotExist:
            return Response({"error":"This organization is not exists"},status=status.HTTP_403_FORBIDDEN)   


    def put(self,request,pk):
        datas = organization.objects.get(pk=pk)
        serializer = organization_Serializer(datas,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)                   