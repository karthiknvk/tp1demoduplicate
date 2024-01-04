from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addreview(request):
  return render(request,'addreview.html')

@login_required
def addspot(request):
  return render(request,'addspot.html')

def showreview(request):
  pass