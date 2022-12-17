from django.db import models

# Create your models here.

# CHARFIELD  
# INTGERFIELD 
# DATETIMEFIELD () 
# IMAGEFIELD () 
# EMAIL_FIELD()

class RollerTable(models.Model):
    uid=models.IntegerField(null=True)
    plant_code=models.CharField(max_length=255)
    zone=models.CharField(max_length=255)
    description=models.CharField(max_length=50) 
    date_of_start=models.DateTimeField(auto_now_add=True,null=True,blank=True)


    
# # python manage.py makemigrations 

# python manage.py makemigrations joinapp1 (python-- sql queries )
#python manage.py migrate --(sql queries execution)
    
    
    
    
    

