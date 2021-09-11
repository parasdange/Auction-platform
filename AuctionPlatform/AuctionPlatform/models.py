from django.db import models

from django.contrib.auth.models import User

class UserInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	mobile=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	password=models.CharField(max_length=30)