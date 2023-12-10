from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thread(models.Model):
    title = models.CharField('Title', max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField('Content')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.thread


class Contact(models.Model):

    name = models.CharField('User name', max_length=50)
    email = models.EmailField('User email')
    message = models.TextField('User Message')

    def __str__(self) -> str:
        return self.name
