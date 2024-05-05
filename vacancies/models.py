from django.db import models

from authentication.models import User

# Create your models here.

class VacancyCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='vacancies')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(VacancyCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='vacancies')
    image_url = models.FileField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name