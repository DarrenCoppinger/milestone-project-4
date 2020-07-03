from django.db import models
from django.urls import reverse

class Product(models.Model):
    """ Model for drinks available """
    PINTS = 'Pints'
    BOTTLES = 'Bottles'
    SOFT_DRINKS = 'Soft-Drinks'
    COCKTAILS = 'Cocktails'
    SPIRITS = 'Spirits'

    CATEGORY_CHOICES = [
        (PINTS, 'Pints'),
        (BOTTLES, 'Bottles'),
        (SOFT_DRINKS, 'Soft-Drinks'),
        (COCKTAILS, 'Cocktails'),
        (SPIRITS, 'Spirits'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=PINTS,
    )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    # def get_product_url(self):
    #     """ Gets product url iusing id as pk """
    #     return reverse('product-description', kwargs={'pk': self.id})

    def __str__(self):
        return self.name
