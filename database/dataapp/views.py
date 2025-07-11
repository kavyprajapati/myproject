import os
import uuid
from django.http import HttpResponse
from django.shortcuts import render,redirect
from dataapp.models import *
from database import settings

# Create your views here.
def home(request):
  
    u = UserMaster(
        usrName = "kavy",
        usrEmail = 'pkavy121@gmail.com',
        usrPassword = 123412
        )
    u.save()
    return render(request, 'home.html')

def catList(request):
    cat = list(categoryMaster.objects.all())
    
    return render(request,"category/index.html",{'cat':cat})

def catCreate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        seqno = request.POST.get('seqno')
        slug = name.lower().replace(" ","_")

        isExist = categoryMaster.objects.filter(catName = name)
        if isExist:
            errorMsg = "Category is already exist"
            return render(request,"category/create.html", {"errorMsg":errorMsg})
        else:
            isSeqno = categoryMaster.objects.filter(catSeqno = seqno)
            if isSeqno:
                errorMsg = "seq no is already exist"
                return render(request,"category/create.html", {"errorMsg":errorMsg})
        cat = categoryMaster(
            catName=name,
            catSlug=slug,
            catSeqno=seqno

        )
        cat.save()
        return redirect('/manage/categories')
    return render(request,"category/create.html")


def catdelete(request, id):
    data = categoryMaster.objects.get(id = id)
    data.delete()
    return redirect('/manage/categories/')


def editCat(request,id):
    catData = categoryMaster.objects.get(id=id)
    
    if request.method == "POST":
        name = request.POST.get("name")
        cId = request.POST.get("id")
        seqno = request.POST.get("seqno")
        slug  = name.lower().replace(" ","-")
        status = True
        if request.POST.get("Status") == None:
            status=False
        isSeqno = categoryMaster.objects.filter(catSeqno=seqno).first()
        print(isSeqno.id," = =",cId)
        if isSeqno:
            id1 = str(isSeqno.id)
            id2 = str(cId)
            if id1==id2:
                catData.catName=name
                catData.catSlug=slug
                catData.catSeqno=seqno
                catData.catStates=status
                catData.save()
                return redirect('/manage/categories')
            else:
                errorMsg = "Seq No is already exist."
                return render(request,"category/edit.html",             {"errorMsg":errorMsg,"data":catData})
            
          
    return render(request,"category/edit.html",{"data":catData})


def catImage(request):
    if request.method == "POST":
        fle = request.FILES.get('catImage')
        print(fle,"image")
        
        ext = os.path.splitext(fle.name)[1]
        a = f"{ext}"
        print(a)
        fileName = f"{uuid.uuid4().hex}{ext}"
        path = os.path.join(settings.MEDIA_ROOT,fileName)
        
        with open(path,'wb+') as destination:
            for chunk in fle.chunks():
                destination.write(chunk)
    return render(request,"/manage/categories")