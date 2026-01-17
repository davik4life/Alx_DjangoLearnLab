from django.db import models
"""
Create a Django model called Product with fields like name, description, price, and category.
Use the Django ORM to create, retrieve, update, and delete Product instances.
Write queries to filter products by category and order them by price.
Configure a MySQL database connection in your Django project settings.
Install the required MySQL driver (mysqlclient).
Run the migrate command to create the necessary tables in the database.
"""
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length= 100)
    description = models.CharField(max_length=400)
    price = models.FloatField
    category = models.Field

