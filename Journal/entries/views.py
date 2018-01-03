from django.shortcuts import render

# Create your views here.
def Homepage(request):
    template_name = 'home'
    return render(request,'home.html')