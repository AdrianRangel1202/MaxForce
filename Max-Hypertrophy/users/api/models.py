from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models




class UserManager(BaseUserManager):
    def main_create_user(self, username, email, name,last_name,password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self.main_create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self.main_create_user(username, email, name,last_name, password, True, True, **extra_fields)

    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 150, unique= True)
    email = models.EmailField(max_length = 150, unique= True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null =True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null= True)
    password = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

   
    def __str__(self):   
        return f'{self.username}'