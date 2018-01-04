from django.db import models

class User(models.Model):
    screen_name = models.CharField(max_length=125)
    email = models.EmailField()
    

class Post(models.Model):
    user_name = User.screen_name
    post_title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.post_title

