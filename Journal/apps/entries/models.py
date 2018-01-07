from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class User(models.Model):
    screen_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.screen_name


class Post(models.Model):
    poster_name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=500,default='SOME STRING')
    # redirect_url = 'post_list.html'
    # def get_absolute_url(self):
    #     return reverse("post_list", kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title
