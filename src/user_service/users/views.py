from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer, UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy', 'service': 'user-service'})