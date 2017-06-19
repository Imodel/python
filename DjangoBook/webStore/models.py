#coding:utf8
from __future__ import unicode_literals

from django.db import models
import os
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

def get_image_path(instance,filname):
    return os.path.join('pic_folder',str(instance.id),filname)

# Create your models here.
class Product(models.Model):
    TYPE = (
        ('1','书籍'),
        ('2','电子')
    )
    name = models.CharField(max_length=64,verbose_name='商品名称')
    type = models.CharField(max_length=1,choices=TYPE,verbose_name='商品类型')
    price = models.DecimalField(max_digits=11,decimal_places=2,verbose_name='商品价格')
    image = models.ImageField(upload_to='pic_folder',default='pic_folder/None/no-image.jpg',verbose_name='商品图片')
    image_thumbnail = ImageSpecField(source='image',processors=[ResizeToFill(100,50)],format='JPEG',options={'quality':60})
    date = models.DateField(auto_now_add=True,verbose_name='发布时间')
    content = models.TextField(blank=True,verbose_name='商品内容')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-date']
        verbose_name='商品'
        verbose_name_plural='商品'



