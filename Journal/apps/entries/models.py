from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class User(models.Model):
    screen_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.screen_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=500,default='SOME STRING')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)

    def get_absolute_url(self):
        return reverse('thanks')