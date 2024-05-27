from django.shortcuts import render
from .models import Destination
from django.views import View

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})

class Morocco(View):
    def get(self,request):
        return render(request,'Morocco.html',{})
class Brazil(View):
    def get(self,request):
        return render(request,'Brazil.html',{})
    
def destinations(request):
    return render(request, 'destinations.html')

def index(request):
    return render(request, 'index.html')

def marseille(request):
    return render(request, 'Marseille.html')

def travel(request):
    return render(request, 'travel.html')

def travel2(request):
    return render(request, 'travel2.html')    