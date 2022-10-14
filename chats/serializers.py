from rest_framework import serializers
from .models import *


class model_Chat_Serializer(serializers.ModelSerializer):
    class Meta:
        model = model_Chat
        fields = "__all__"


class organization_Serializer(serializers.ModelSerializer):
    model_chat = model_Chat_Serializer()
    class Meta:
        model = organization
        fields = "__all__"        



class department_Serializer(serializers.ModelSerializer):
    model_chat = model_Chat_Serializer()
    
    class Meta:
        model = Department
        fields = "__all__"                