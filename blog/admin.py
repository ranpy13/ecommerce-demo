from django.contrib import admin
from .models import blog ,Category , review
# Register your models here.
admin.site.register(blog)
admin.site.register(Category)
admin.site.register(review)