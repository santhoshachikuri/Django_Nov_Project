from rest_framework import serializers
from .models import *


class RollerSerializer(serializers.ModelSerializer):
    class Meta:
        model=RollerTable
        fields='__all__'
    
    

