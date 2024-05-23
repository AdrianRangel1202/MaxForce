from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models



class UserManager(BaseUserManager):
    def main_create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self.main_create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self.main_create_user(username, email, password, True, True, **extra_fields)

    
class User(AbstractBaseUser):
    username = models.CharField(max_length = 100, unique= True)
    email = models.EmailField(max_length = 100, unique= True)
    password = models.CharField(max_length = 100)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

   
    def __str__(self):   
        return f'{self.username}'