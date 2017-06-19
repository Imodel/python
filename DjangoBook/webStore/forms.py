#coding:utf8

from django import forms
from models import *

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name','price','type','content','image']