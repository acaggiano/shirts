from django.shortcuts import render
from django.http import HttpResponse
from .models import Shirt

# Create your views here.

def index(request):
    # recent = Shirt.objects.filter(worn=True)[:5]
    context = {}
    return render(request, 'shirts/index.html', context)

def reset(request):
    Shirt.objects.update(worn=False)
    
    response = HttpResponse("All shirts unworn")
    response.status_code = 200

    return response  
