from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from .models import Product
from .forms import ProductFrom
import datetime

# Create your views here.

class ProductView():
    def save(self,request):
        data = request.data
        Product.objects.create(**data)

def index(request):
    products = Product.objects.all()
    context = Context({'product_list':products})
    return render(request,'product_list.html',context)

def get(request,id):
    product = Product.objects.get(id=int(id))
    context = Context({'product':product})
    return render(request,'product_detail.html',context)

def add(request):
    if request.method=='POST':
        form = ProductFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    products = Product.objects.all()
    context = Context({'product_list': products})
    return render(request, 'product_list.html', context)


def addHtml(request):
    form = ProductFrom()
    return render(request,'product_add.html',{'form':form})
