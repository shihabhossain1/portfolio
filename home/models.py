from django.db import models

# Create your models here.
class Contact_me(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    added_on = models.DateTimeField(auto_now_add=True)