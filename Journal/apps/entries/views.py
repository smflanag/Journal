from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from Journal.apps.entries.models import User, Post
from Journal.apps.entries.forms import PostForm


def Homepage(request):
    template_name = 'home'
    post_list_context = {'post_list':Post.objects.all()}
    return render(request, 'home.html', context=post_list_context)


def Login(request):
    template_name = 'login'
    return render(request, 'login.html')

def Thanks(request):
    template_name = 'thanks'
    return render(request, 'thanks.html')


def ContactUs(request):
    template_name = 'contact_us'
    return render(request, 'contact_us.html')


class PostCreate(CreateView):
    redirect_field_name = 'post_form.html'
    form_class = PostForm
    model = Post


class PostList(ListView):
    redirect_url = 'home.html'
    form_class = PostForm
    model = Post
    # queryset = Post.objects.order_by('-created')


class PostDetail(DetailView):
    model = Post
