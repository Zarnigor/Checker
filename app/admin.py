from django.contrib import admin
from app.models import Problem, Submission


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    pass