from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('hire_me/', hire_me, name='hire_me'),
    path('contact/', contact_me, name='contact_me')
]
