from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Post,User,Like
from .forms import PostForm
from django.core.paginator import Paginator

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = request.user
            post.save()
            return redirect('postList')
    else:
        form = PostForm()
        return render(request, 'CRUD/new.html', {'form':form})

def main(request):
    like_list = Post.objects.all().order_by('-like_counting')[:10]
    return render(request, 'CRUD/main.html', {'likes':like_list})

def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    plan_object = Post.objects.get(id=post_id)
    plan_object.view_counting = plan_object.view_counting+1
    plan_object.save()
    like = Like.objects.filter(user=request.user, post = post)
    return render(request, 'CRUD/show.html', {'post': post, 'like':like})

def like(request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    liked =  Like.objects.filter(user=request.user, post=post)
    if not liked:
        Like.objects.create(user=request.user, post=post)
        post.like_counting += 1
        post.save()
    else:
        liked = Like.objects.get(user=request.user, post=post)
        post.like_counting -= 1
        post.save()
        liked.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def edit(request):
    return render(request,'CRUD/edit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('postList')
    else:
        form  = PostForm(instance=post)
        return render(request, 'CRUD/edit.html',{'form':form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()  
    return redirect('postList')
    
def postList(request):
    plans = Post.objects
    sort = request.GET.get('sort','')
    plan_list = Post.objects.all()
    if sort == 'like':
        plan_list = Post.objects.all().order_by('-like_counting', 'created_at')
    elif sort == 'view':
        plan_list = Post.objects.all().order_by('-view_counting', '-created_at')
    elif sort == 'writedate':
        plan_list = Post.objects.all().order_by('created_at')
    paginator = Paginator(plan_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'CRUD/postList.html', {'plans':plans, 'posts':posts })   