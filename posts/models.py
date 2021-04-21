from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
        )
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return self.author.username
    
    def get_absolute_url(self):
       return reverse('post-detail', kwargs={'pk': self.pk})
    

    
