from django.db import models

# Create your models here.

class InventoryItem(models.Model):
    product_id = models.IntegerField(unique=True)
    quantity = models.IntegerField(default=0)
    reserved = models.IntegerField(default=0)
    warehouse_location = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def available(self):
        return self.quantity - self.reserved
    
    class Meta:
        ordering = ['-product_id']