from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
	catname=models.CharField(max_length=50)


class Product(models.Model):
	name=models.CharField(max_length=100)
	price=models.DecimalField(decimal_places=2,max_digits=12)
	# qty=models.IntegerField()
	city=models.CharField(max_length=20)
	des=models.CharField(max_length=700)
	closing_date=models.CharField(max_length=20)
	cat=models.ForeignKey(Category,on_delete=models.CASCADE)
	cover_img=models.ImageField(upload_to="product_image",blank=True)
	current_date=models.DateTimeField(auto_now=True)
	added_by=models.ForeignKey(User,on_delete=models.CASCADE)


class Product_images(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	product_images=models.ImageField(upload_to="product_image",blank=True)

class City(models.Model):
	city=models.CharField(max_length=20,unique=True)

class Feedback(models.Model):
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	mobile=models.CharField(max_length=30)
	comment=models.CharField(max_length=200)
	send_by=models.ForeignKey(User,on_delete=models.CASCADE)


