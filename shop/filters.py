import django_filters
from .models import clothe

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = clothe
        fields = ['price','puplish_at',]
  