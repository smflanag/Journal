from django import forms
from django.forms import ModelForm
from Journal.apps.entries.models import User, Post


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['screen_name', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['poster_name', 'title', 'post_content']