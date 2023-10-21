from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home/home.html')

def hire_me(request):

    return render(request, 'home/hire_me.html')

def contact_me(request):

    return render(request, 'home/contact.html')