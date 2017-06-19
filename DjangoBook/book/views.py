from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from book.models import Book
import datetime
# Create your views here.

def hello(request):
    return HttpResponse('Hello world')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s .</body></html>" % now
    return HttpResponse(html)

def hours_head(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> It %s hour(s),it will be %s .</body></html>" % (offset,dt)
    return HttpResponse(html)

def tem_date(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Enter a search term')
        elif len(q) >20 :
            error.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__contains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})

    return render_to_response('search_form.html',{'errors':error})