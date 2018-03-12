from django.urls import path, include
from . import drf_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', drf_views.UserViewSet)
router.register(r'groups', drf_views.GroupViewSet)
router.register(r'shirts', drf_views.ShirtViewSet, 'shirts')

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='shirt_rest_framework'))
]
