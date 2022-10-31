from threading import Thread
from django.shortcuts import render
from .models import Company, Three,Team,First
# Create your views here.
def aboutus(request):
    context = {
        'first':First.objects.last(),
        'Third':Three.objects.all(),
        'team':Team.objects.all(),
        'comp':Company.objects.all(),
    }
    return render(request,'aboutus/aboutus.html',context)