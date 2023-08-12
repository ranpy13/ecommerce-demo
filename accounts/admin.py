from re import A
from django.contrib import admin

# Register your models here.
from .models import City , Profile

admin.site.register(Profile)
admin.site.register(City)