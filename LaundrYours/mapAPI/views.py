from django.shortcuts import render

from .models import laundry_location

# Create your views here.

def showMap(request):
    loc = laundry_location.objects.all()
    context = {
        'loc' : loc,
    }
    return render(request,'laundry.html',context)