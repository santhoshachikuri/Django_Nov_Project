from django.db import models

from joinapp2.manager import CustomUserManager
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin


class B2CUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255,null=True)
    role=models.CharField(max_length=255,null=True)
    status=models.CharField(max_length=255,null=True)
    date_join=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['role','name']
    objects=CustomUserManager()
    
    def __str__(self) :
        return '(%s,%s,%s)' % (self.email,self.name,self.role)
