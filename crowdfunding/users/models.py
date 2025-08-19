from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):

    def __str__(): 
        return self.username 
        