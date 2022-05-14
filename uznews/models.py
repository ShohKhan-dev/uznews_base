from django.db import models
from django.contrib.auth.models import User

# Create your models here. 


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')







class Keywords(models.Model):
    word = models.CharField(max_length=125)
    users = models.ManyToManyField(User, related_name='members')
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.word






class WatchList(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word
    
class IgnoreList(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word


class WaitList(models.Model):
    word = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.word



class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    views = models.IntegerField()
    category = models.CharField(max_length=25, null=False, blank=True)
    posted_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-posted_at',)
    




    
from django.contrib.auth.models import User

class Notification(models.Model):

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']