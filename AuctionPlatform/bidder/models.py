from django.db import models

from  django.contrib.auth.models import User

from seller. models import Product

class Bidder_product(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	bid_by = models.ForeignKey(User,on_delete=models.CASCADE)
	bid_amount=models.DecimalField(decimal_places=2,max_digits=12)
	bid_date=models.DateTimeField(auto_now=True)
	status = models.IntegerField(default=0)
	place_status=models.IntegerField(default=0)


class Pyment_method(models.Model):
	method=models.CharField(max_length=30)


class Orders(models.Model):
	order_id=models.CharField(max_length=100)

	bid=models.ForeignKey(Bidder_product,on_delete=models.CASCADE)

	product_name=models.CharField(max_length=50)

	order_date=models.DateTimeField(auto_now=True)

	total_amt=models.DecimalField(max_digits=10,decimal_places=3)

	amt_status=models.IntegerField(default=0)

	order_status=models.IntegerField(default=0)

	address=models.CharField(max_length=50)

	payment_method=models.CharField(max_length=30)
# Create your models here.
