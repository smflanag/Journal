from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


from Journal.apps.entries.models import User, Post
from Journal.apps.entries.forms import PostForm, UserForm, ContactForm


def Homepage(request):
    template_name = 'home'
    post_list_context = {'post_list':Post.objects.all()}
    return render(request, 'home.html', context=post_list_context)


def Login(request):
    screen_name = request.POST['screen_name']
    password = request.POST['password']
    User = authenticate(request, screen_name, password)
    if User is not None:
        login(request, User)
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    if not request.user.is_authenticated:
        return render(request, 'login.html')

from django.contrib.auth import logout

def Logout(request):
    logout(request)
    return render('home.html')


def Thanks(request):
    template_name = 'thanks'
    return render(request, 'thanks.html')


def Contact(request):
    form_class = ContactForm
    redirect_field_name = 'thanks.html'
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name','')
            contact_email = request.POST.get('contact_email','')
            form_content = request.POST.get('content','')

            template = get_template('contact_template.txt')
            context = {'contact_name': contact_name,
                               'contact_email': contact_email,
                               'form_content': form_content,}
            content = template.render(context)

            email = EmailMessage("new contact form submission",
                                 content, "Your Website" +'',
                                 ['smflanag@gmail.com'],
                                 headers = {'Reply-To': contact_email})
            email.send()
            return redirect('contact_us.html')
    return render(request, 'contact_us.html', {'form':form_class})


class PostCreate(LoginRequiredMixin,CreateView):
    redirect_field_name = 'post_form.html'
    form_class = PostForm
    model = Post


class PostList(ListView):
    redirect_url = 'home.html'
    form_class = PostForm
    model = Post


class PostDetail(DetailView):
    model = Post


class UserCreate(CreateView):
    form_class = UserForm
    redirect_field_name = 'login.html'
    model = User
