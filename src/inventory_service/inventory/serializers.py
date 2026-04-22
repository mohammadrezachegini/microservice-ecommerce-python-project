from rest_framework import serializers
from .models import InventoryItem

class InventorySerializer(serializers.ModelSerializer):
    available = serializers.ReadOnlyField()  # exposes the @property

    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['id', 'updated_at']