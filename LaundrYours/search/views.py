from django.shortcuts import render
from .models import Fiber

# Create your views here.
def home(request):
    return render(request, 'home.html')

def fiberResult(request):
    fiber_object = Fiber.objects.all()
    fibersearch = request.GET.get('query','')
    if fibersearch : 
        fiber_object = fiber_object.filter(name__icontains= fibersearch)
    return render(request, 'result.html', {'fiber':fiber_object, 'fibersearch': fibersearch})