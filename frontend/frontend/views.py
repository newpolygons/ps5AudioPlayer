import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404



def index(request):
    return render(request, 'frontend/index.html')
