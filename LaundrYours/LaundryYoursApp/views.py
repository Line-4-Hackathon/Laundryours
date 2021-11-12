from django.shortcuts import redirect, render, get_object_or_404

from .models import Post
from django.utils import timezone
# Create your views here.

def main(request):
    context = {

    }
    return render(request,'main.html',context)

def createPage(request):
    # context = {

    # }
    return render(request,'create.html')

def create(request):
    new_data = Post()
    new_data.title = request.POST['title']
    new_data.writer = request.POST['writer']
    new_data.pub_date = timezone.now()
    new_data.body = request.POST['body']
    new_data.save()
    return redirect('createPage')

def detail(request,id):
    detail_data = get_object_or_404(Post, pk = id)
    context = {
        'title':detail_data.title,
        'writer':detail_data.writer,
        'body':detail_data.body,
        'pub_date':detail_data.pub_date,
        'id':id,
    }
    return render(request,'detail.html',context)

def updatePage(request,id):
    update_data = get_object_or_404(Post, pk=id)
    context = {
        'title':update_data.title,
        'writer':update_data.writer,
        'body':update_data.body,
        # 'image':update_data.image,
        'id':id,
    }
    return render(request,'update.html',context)

def update(request, id):
    update_data = get_object_or_404(Post, pk=id)
    update_data.title = request.POST['title'] 
    update_data.writer = request.POST['writer']
    update_data.body = request.POST['body']
    update_data.pub_date = timezone.now()
    # update_data.image = request.FILES['image']
    update_data.save()
    return redirect('main')

def delete(request, id):
    delete_data = get_object_or_404(Post, pk=id)
    delete_data.delete()
    return redirect('main')


