"""DjangoBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from book.views import *
from webStore.views import *
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_head),
    url(r'^time/tmp/$', tem_date),
    url(r'^search-form/$',search_form),
    url(r'^search/$',search),
    url(r'^index/$',index),
    url(r'^get/(.*)',get),
    url(r'^addHtml/$',addHtml),
    url(r'^add/$',add)
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
