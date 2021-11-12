from django.shortcuts import render 
from django.http import JsonResponse 
    
import json 

def index(request): 
    return render(request, 'vueTest/index.html', {})

# def list(request): 
#     vueTests = VueTest.objects.all() 
#     vueTest_list = [] 
    
#     for index, vueTest in enumerate(vueTests, start=1): 
#         vueTest_list.append({'id':index,'title':vueTest.title,'completed':vueTest.completed}) 
        
#     return JsonResponse(vueTest_list, safe=False) 