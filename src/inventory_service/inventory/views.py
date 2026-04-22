from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import InventoryItem
from .serializers import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventorySerializer
    
    @action(detail=True, methods=['post'])
    def reserver(self, request, pk=None):
        item = self.get_object()
        qty = request.data.get('quantity', 0)
        if item.available < qty:
            return Response({'error': 'Not enough inventory available'}, status=status.HTTP_400_BAD_REQUEST)
        item.reserved += qty
        item.save()
        return Response(InventorySerializer(item).data)
    
    @action(detail=True, methods=['post'])
    def release(self, request, pk=None):
        item = self.get_object()
        qty = request.data.get('quantity', 0)
        item.reserved = max(0, item.reserved - qty)
        item.save()
        return Response(InventorySerializer(item).data)


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy', 'service': 'inventory-service'})
