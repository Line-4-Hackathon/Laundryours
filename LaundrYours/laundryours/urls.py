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
from django.urls import path
from LaundryYoursApp.views import main,createPage,create,detail,updatePage,update,delete
from mapAPI.views import showMap
from search.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',main,name='main'),
    path('create/',create,name='create'),
    path('createPage/',createPage,name='createPage'),
    path('detail/<id>',detail,name='detail'),
    path('updatePage/<id>',updatePage,name='updatePage'),
    path('update/<id>',update,name='update'),
    path('delete/<id>',delete,name='delete'),
    path('showMap',showMap,name='showMap'),
    path('', home, name="home"),
    path('research/', fiberResult, name="fiberResult"),
]
