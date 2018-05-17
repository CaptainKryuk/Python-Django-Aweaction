from django.db import models
from django.contrib.auth.models import User


# Expanding user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)
    direction = models.CharField(max_length=20)


class Projects(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300)
    document = models.FileField(upload_to='projects/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
