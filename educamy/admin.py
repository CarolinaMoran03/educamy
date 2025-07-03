from django.contrib import admin
from .models import SchoolSubject, GeneratedContent, AnualPlan, MicroPlan, Quiz

# Register your models here.
admin.site.register(SchoolSubject)
admin.site.register(GeneratedContent)
admin.site.register(MicroPlan)
admin.site.register(AnualPlan)
admin.site.register(Quiz)
