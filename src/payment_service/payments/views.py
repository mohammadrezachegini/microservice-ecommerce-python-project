import uuid
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def perform_create(self, serilizer):
        serilizer.save(
            transaction_id = str(uuid.uuid4()),
            status='completed'
        )
    
    @action(detail=True, methods=['post'])    
    def refund(self, request, pk=None):
        payment = self.get_object()
        if payment.status != 'completed':
            return Response({'error': 'Only completed payments can be refunded.'}, status=status.HTTP_400_BAD_REQUEST)
        payment.status = 'refunded'
        payment.save()
        return Response(PaymentSerializer(payment).data)


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy', 'service': 'payment-service'})