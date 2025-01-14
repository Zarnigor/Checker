from django.contrib import admin
from app.models import Problem


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass