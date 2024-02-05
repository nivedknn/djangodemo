from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from shop.models import Category, Product
from django.contrib.auth.decorators import login_required


def allcategory(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def view(request,p):
    p= Product.objects.get(name=p)
    return render(request, 'view.html', {'p':p})

def allproduct(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':p})

def user_login(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        User = authenticate(username=u, password=p)
        if User:
            login(request,User)
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:user_login')



def register(request):
    if(request.method == "POST"):
        u=request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']

        if(p==c):
            user=User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            user.save()
            return redirect("shop:allcat")
        else:
            return HttpResponse("passwords are not same")
    return render(request,'register.html')

