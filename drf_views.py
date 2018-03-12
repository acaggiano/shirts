from django.contrib.auth.models import User, Group
from .models import Shirt
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ShirtSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ShirtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows goals to be viewed or edited
    """
    serializer_class = ShirtSerializer
    
    def get_queryset(self):
        queryset = Shirt.objects.all()
        param_worn = self.request.query_params.get('worn', None)
        if param_worn is not None:
            queryset = queryset.filter(worn=param_worn)
        return queryset
    
