from rest_framework import serializers 
from rest_framework.validators import UniqueValidator 
from .models import * 
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
## Signup Serializer

# ORM Queries :
# CRUD 

# Readd
# modelsname.objects.all()
# modelsname.objects.get(marks=450 )
# models.objects.filter(marks>400)


class RegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True,
        validators=[UniqueValidator(queryset=B2CUser.objects.all())])
    password=serializers.CharField(required=True,min_length=8,write_only=True)
    name=serializers.CharField(required=True)
    role=serializers.CharField(required=True)
    status=serializers.CharField(required=True)
    
    def create(self,validated_data):
        try:
            user=B2CUser.objects.get(email=validated_data["email"],
                name=validated_data["name"],role=validated_data["role"],status=validated_data["status"])
            raise ValidationError({"response": "User Already Existed Please Login"})
        except B2CUser.DoesNotExist:
            user=B2CUser.objects.create_user(**validated_data)
            return user
            
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True,min_length=8)
    
    def validate(self,validated_data):
       user=B2CUser.objects.filter(email=validated_data["email"]) 
       if not user.exists():
           raise serializers.ValidationError({"email":"Email Not Found"}) 
       if not check_password(validated_data["password"],user.first().password):
           raise serializers.ValidationError({"password":"Incorrect Password"})
       return validated_data
           
    
    
class ChangePasswordSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True,min_length=8)
    newpassword=serializers.CharField(required=True,min_length=8) 
    def validate(self,validated_data):
       user=B2CUser.objects.filter(email=validated_data["email"]) 
       if not user.exists():
           raise serializers.ValidationError({"email":"Email Not Found"}) 
       if not check_password(validated_data["password"],user.first().password):
           raise serializers.ValidationError({"password":"Incorrect Password"})
       return validated_data





class B2CUSerSerializer(serializers.ModelSerializer):
    class Meta:
        model=B2CUser
        fields='__all__'
    
    