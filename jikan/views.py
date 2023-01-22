from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from django.contrib import messages
from django.urls import reverse_lazy
from django.conf import settings
# Create your views here.




# home page url - home page ur  
def home(request): 
    return render(request, 'jikan/home.html')



def search_anime(request): 
    id1 = request.GET.get('q')  
    response = requests.get("https://api.jikan.moe/v4/anime/" + id1)     
    if response.status_code == 404: 
        messages.error(request, 'Your anime chracter doesnt exist please tty anot number like 118') 
        return render(request, 'jikan/home.html') 
    else: 
        z = response.json() 
        context = {
            'z' : z,
        } 
        return render(request, 'jikan/search_anime.html', context)

