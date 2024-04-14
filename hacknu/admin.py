from django.contrib import admin

# Register your models here.

from .models import QuizStatement, QuizQuestions, QuizInstance


class QuizQuestionsInline(admin.StackedInline):
    model = QuizQuestions
    

@admin.register(QuizStatement)
class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [QuizQuestionsInline]

@admin.register(QuizInstance)
class QuizInstanceAdmin(admin.ModelAdmin):
    pass
   