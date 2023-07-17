from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    dictanory = {'niralee':"code coming from views.py file"}
    return render(request,'first_app/index.html',context=dictanory)
