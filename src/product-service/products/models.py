from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(promary_key=True)
    name = models.charField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'products'
        managed = False
        
    def __str__(self):
        return self.name 