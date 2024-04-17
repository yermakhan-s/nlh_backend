from django.db import models
from authentication.models import User

# Create your models here.

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.FileField(null=True, blank=True)
    created_date =models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
