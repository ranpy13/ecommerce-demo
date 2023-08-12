from django.db import models

# Create your models here.
class Info(models.Model):
    """Model definition for Info."""
    place=models.CharField(max_length=70)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=254)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Info."""

        verbose_name = 'Info'
        verbose_name_plural = 'Infos'

    def __str__(self) :
        return self.email

   