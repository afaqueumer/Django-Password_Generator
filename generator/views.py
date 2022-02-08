from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render( request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    val_val = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    if request.GET.get('specialchar'):
        characters.extend(list('#@^%&*'))
    
    leng = int(request.GET.get('length'))
    for a in range(leng):
        val_val += random.choice(characters)
    
    return render( request, 'generator/pwd.html', {'key_key':val_val})
