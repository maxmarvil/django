from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render_to_response,render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
from mysite.models import Category
from django.contrib import auth


def home(request):
    category = Category.objects.all()
    context ={
        'category':category,
        'username': auth.get_user(request).username,
    }
    return render(request,'mysite/home.html', context)

def about(request):
    return render(request,"mysite/about.html")

def show_category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    return render(request, "mysite/category.html",{'category':category})

