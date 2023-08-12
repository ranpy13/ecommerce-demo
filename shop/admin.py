from django.contrib import admin

from shop.forms import ColorForm
from .models import Color, clothe ,Category ,review,Size
# Register your models here.
admin.site.register(clothe)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(review)

class ColorAdmin(admin.ModelAdmin):
    form = ColorForm
admin.site.register(Color, ColorAdmin)

