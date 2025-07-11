# project/urls.py
from django.contrib import admin
from django.urls import path

from dboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('user/',views.user, name='user'),
    path('setting/',views.setting, name='setting'),
    path('login_p/',views.login_p, name='login_p'),
    path('logout/',views.logout, name='logout'),
    path('category/',views.category, name='category'),
    path("category_add/",views.category_add,name="category_add"),
    path("/delte_category/<id>/",views.delte_category,name= "delte_category"),
]
