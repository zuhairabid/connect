from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg',upload_to='profile_pics')
    cover_img = models.ImageField(upload_to='cover_pics',default='default.png')
    
    def __str__(self):
        return f'{self.user.username} Profile'