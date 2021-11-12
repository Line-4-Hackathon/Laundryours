"""laundryours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import accounts.views
import search.views
import CRUD.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search.views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('CRUD/<int:post_id>', CRUD.views.show, name='show'),
    path('CRUD/new', CRUD.views.new, name='new'),
    path('CRUD/edit',CRUD.views.edit, name ="edit"),
    path('CRUD/postList', CRUD.views.postList, name='postList'),
    path('postupdate/<int:post_id>',CRUD.views.postupdate, name='postupdate'),
    path('like/<int:post_id>',CRUD.views.like, name='like'),
    path('delete/<int:post_id>',CRUD.views.delete,name='delete'),
]
