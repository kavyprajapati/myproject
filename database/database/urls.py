"""
URL configuration for database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from dataapp import views
from database import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("home/", views.home),
    path('manage/categories/',views.catList,name="categoryList"),
    path('manage/category/create',views.catCreate,name="categoryCreate"),
    path("manage/category/editCat/<str:id>/",views.editCat,name= "editCat"),
    path("manage/category/catdelete/<str:id>/",views.catdelete,name= "catdelete"),
    path("manage/category/catImage/",views.catImage,name= "catImage"),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
