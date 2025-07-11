"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from myapp import views
from foodapp import views
from minapp import views
from flowerapp import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),  # Home page url
    
    # path("home/", views.home, name="home"),
    # path("demo1/", views.demo1, name="demo1"),
    # path("new1/", views.new1, name="new1"),
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    # path("home1/", views.home1, name="home1"),
    # path("about1/", views.about1, name="about1"),
    # path("contact1/", views.contact1, name="contact1"),
    # path("food/",views.food,name="food"),
    # path("aryan/",views.aryan, name="aryan"),
    # path('food/delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    # path('food/update_recipe/<int:id>/', views.update_recipe, name='update_recipe'),
    # path("login/",views.login,name="login"),
    # path("register/",views.register,name="register"),
    # path('cars/',views.cars, name="cars"),
    # path('contacts/', views.contacts, name='contacts'),
    # path('home2/', views.home2, name='home2'),
    # path('about2/', views.about_view, name='about2'),
    # path('shop2/', views.shop2, name='shop2'),
    # path('contacts1/', views.contacts1, name='contacts1'),
    # path('login1/', views.login1, name='login1'),
    # path('signup1/', views.signup1, name='signup1'),

    path('w_home/', views.w_home, name="w_home"),
    path('W_about/', views.W_about, name="W_about"),
    path('W_shop/', views.W_shop, name="W_shop"),
    path('W_contact/', views.W_contact, name="W_contact"),
    path('login/', views.login, name='login'),
    path('sign_up/',views.sign_up,name="sign_up"),

    path('myadmin/',include('dboard.urls')),
    # path('',include('dataapp.urls'))
    
    
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)