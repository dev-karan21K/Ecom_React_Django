from django.db import models
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=25)
    car_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cat_name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    stock = models.PositiveIntegerField()
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name