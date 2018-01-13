from django import forms
from django.forms import ModelForm
from Journal.apps.entries.models import User, Post, Contact


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['screen_name', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_content']


class ContactForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Contact
        fields = ['contact_name','contact_email','content']