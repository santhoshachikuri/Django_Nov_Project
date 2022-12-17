# manager--models-- serialzer --views--url
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations=True 
    
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_('The Email must valid Email'))
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email,name,role,status,password=None):
        return self._create_user(email,password,name=name,role=role,status=status)
        
    