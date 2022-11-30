# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')


