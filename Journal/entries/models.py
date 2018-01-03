from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=125)
    post_title = models.CharField(max_length=50)
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.post_title
