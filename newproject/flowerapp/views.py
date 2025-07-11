from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from .models import*

# Create your views here.

# def home2(request):
#     return render(request, 'website.html')

# def about_view(request):
#     return render(request, 'flowershopabout.html')

# def shop2(request):
#     return render(request, 'flowershopshop.html')

# def contacts1(request):
#     return render(request, 'flowershopcontact.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = User.objects.filter(username=username).first()
#         if user:
#             pwd = (password, user.password)
#             if pwd:
#                 print("Login successful")
#                 return redirect('/aryan/')
#             else:
#                 print("Invalid password")
#         else:
#             print("User not found")
    
        
#     return render(request,"flowershoplogin.html")
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if first_name and last_name and username and password:
#             user = User.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 username = username,
#                 password = password
#                 )
#             user.set_password('password')
#             user.save()
#         else:
#             context = {'erorr: all filds are requird'}
#             return render(request,"flowershopsignup.html",context)
#     return render(request,'flowershopsignup.html')


# def contacts(request):
#     if request.method == 'POST':
#         FullName = request.POST.get('name')
#         EmailAddress = request.POST.get('email')
#         ContactNumber = request.POST.get('contacts')
#         YourMessage = request.POST.get('message')

#         contact.objects.create(
#             FullName = FullName,
#             EmailAddress = EmailAddress,
#             ContactNumber = ContactNumber,
#             YourMessage = YourMessage,
#         )

#     return render(request, 'flowershopcontact.html')


def w_home(request):
    return render(request, 'f_home.html')


def W_about(request):
    return render(request,"f_about.html")


def W_shop(request):
    return render(request,"f_shop.html")


def W_contact(request):
    return render(request,"f_contact.html")


from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method ==  "POST":
        username =request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            pwd = check_password(password, user.password) # type: ignore
            if pwd :
                print("login successful")
                return redirect('/w_home/') # type: ignore
            else:
                print("invalid password")

        else:        
            print("user not found")
        
    return render(request,"f_login.html")




       
def  sign_up(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if name and email and username and password:
            user = User.objects.create_user(
                first_name=name,
                email=email,
                username=username,
                password=password
            )
            user.set_password(password)
            user.save()
            return redirect('/login/')
        else:
            print("please fill all fields")
     

    return render(request,"f_signup.html")
