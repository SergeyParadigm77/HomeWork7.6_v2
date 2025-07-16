from django.contrib.auth.models import AbstractUser
from django.db import models

class ApiUser(AbstractUser):
    ...


class Warehouse(models.Model):
    name = models.CharField(max_length=128)


class Product(models.Model):
    name = models.CharField(max_length=128)
    warehouse = models.ForeignKey(Warehouse, related_name="goods", on_delete=models.CASCADE)


class Booking(models.Model):
    product = models.ForeignKey(Product, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="bookings", on_delete=models.CASCADE)