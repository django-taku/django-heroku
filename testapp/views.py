from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('はじめてのheroku')

