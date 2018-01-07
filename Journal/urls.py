"""Journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url

from Journal.apps.entries import views
# from Journal.apps.entries.views import UserCreate

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.Homepage,name='home'),
    url(r'^create',views.PostCreate.as_view(),name='post_form'),
    url(r'^postlist',views.PostList.as_view(),name='post_list'),
    url(r'^login',views.Login,name='login'),
    url(r'^thanks',views.Thanks,name='thanks'),
    url(r'^contact_us',views.ContactUs,name='contact_us'),
]
