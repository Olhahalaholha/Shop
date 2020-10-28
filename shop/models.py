from django.db import models

# Create your models here.



#	class for admin
class Products(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField()
	discount_price = models.FloatField()
	category = models.CharField(max_length=200)
	description = models.TextField()
	image = models.CharField(max_length=20000)

	def __str__(self):
		return self.title




#	class for admin
class Order(models.Model): 
	items = models.CharField(max_length=300)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=100)
	total = models.CharField(max_length=200)
	bla_bla_bla = models.CharField(max_length=100)
	def __str__(self):
		return self.name