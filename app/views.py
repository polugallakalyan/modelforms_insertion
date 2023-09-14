from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}
    if request.method=='POST':
        DFTO=TopicForm(request.POST)
        if DFTO.is_valid():
            DFTO.save()
            return HttpResponse('topic data inserted')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        DWFO=WebpageForm(request.POST)
        if DWFO.is_valid():
            DWFO.save()
            return HttpResponse('webpage data is inserted')
    return render(request,'insert_webpage.html',d)