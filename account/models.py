from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_pemustaka = models.BooleanField('Is pemustaka', default=False)
    # is_main2 = models.BooleanField('Is main2', default=False)
    
