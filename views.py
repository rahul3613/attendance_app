#from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponseRedirect(reverse('attdc:new',))