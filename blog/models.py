from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    data_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
