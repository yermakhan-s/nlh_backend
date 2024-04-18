from django.contrib import admin

# Register your models here.
from .models import VacancyCategory, Vacancy



class VacancyInline(admin.TabularInline):
    model = Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass

@admin.register(VacancyCategory)
class VacancyCategoryAdmin(admin.ModelAdmin):
    inlines = [VacancyInline]