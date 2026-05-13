from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class BusinessHours(models.Model):
    monday_friday = models.CharField(max_length=100)
    saturday_sunday = models.CharField(max_length=100)

    def __str__(self):
        return "Business Hours"

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return "Contact Info"