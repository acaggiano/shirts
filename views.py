from django.shortcuts import render
from django.http import HttpResponse
from .models import Shirt
from shirtsite.settings import MEDIA_URL

# Create your views here.

def index(request):
    recent = Shirt.objects.filter(worn=True).order_by('-last_worn')[:5]
    context = {'recent': recent, 'media_url': MEDIA_URL}
    return render(request, 'shirts/index.html', context)

def reset(request):
    Shirt.objects.update(worn=False)
    
    response = HttpResponse("All shirts unworn")
    response.status_code = 200

    return response  
