from django.shortcuts import render
from .models import Fiber

# Create your views here.
def home(request):
    return render(request, 'home.html')

def fiberResult(request):
    fiber_object = Fiber.objects.all()
    # query = request.GET.get('query','')
    # if query : 
    #     fiber_object = fiber_object.filter(name__icontains= query)
    return render(request, 'result.html', {'fiber':fiber_object})
