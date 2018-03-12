from django.urls import include, path

from . import views

urlpatterns = [
    path('api/', include('shirts.drf_urls')),
    path('ive_worn_all_my_shirts_once/', views.reset, name='reset'),
    path('', views.index, name='index'),
]
