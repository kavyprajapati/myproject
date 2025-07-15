# views.py
from django.shortcuts import render
from django.shortcuts import redirect, render
from dboard.models import *
from .models import AdminUserMaster
from django.shortcuts import render, redirect, get_object_or_404



# def dashboard(request):
#     return render(request, 'adminpanel.html')

def user(request):
    return render(request, 'user.html')

def setting(request):
    return render(request, 'setting.html')

# def category(request):
#     return render(request, 'catagory.html')

def login_p(request):
    if request.session.get('name'):
        return redirect("/myadmin/dashboard/")
    if request.method ==  "POST":
        mstName =request.POST.get("mstName")
        mstPassword = request.POST.get("mstPassword")
        user = AdminUserMaster.objects.filter(mstName = mstName , mstPassword = mstPassword).first()
        if user:
            request.session['name']= mstName
            return redirect("/myadmin/dashboard/")
        else:
            return redirect('/myadmin/login_p/')
        
        
    return render(request, 'login_p.html')


def dashboard(request):
    if request.session.get('name'):
        return render(request, "adminpanel.html")
    else:
        return redirect("/myadmin/login_p/")

def logout(request):
    request.session.flush()
    return redirect('/myadmin/login_p/')


def category(request):
    tables = cats.objects.all()
    return render(request,"category.html",{"tables":tables})

def category_add(request):
   if request.method == "POST":
        Cate_name = request.POST.get("Cate_name")
        cate_image = request.POST.get("cate_image")
        cate_status = request.POST.get("cate_status")
        cateslug = request.POST.get("cate_cateslug")

        cats.objects.create(
            Cate_name =Cate_name,
            cate_image = cate_image,
            cate_status =cate_status,
            cateslug = cateslug
        )
        return redirect("/myadmin/category/")
   return render(request, 'category_add.html')

def delte_category(request, id):
    query = cats.objects.get(id = id)
    query.delete()
    return redirect("/myadmin/category")

def update(request, id):
    if not request.sessios.get("name"):
        return redirect("/myadmin/login/")
    category = get_object_or_404(category_add, id=id)    
    
    if request.method == "POST":
        category.Cate_name = request.POST.get("Cate_name")




