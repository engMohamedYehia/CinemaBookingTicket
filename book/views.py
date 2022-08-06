from calendar import c
from dataclasses import dataclass
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Subscriber,Movie


# Create your views here.




def main(request):
    name_ = request.POST.get('name')
    birthday_ = request.POST.get('birthday')
    get_movie_name = request.POST.get("m")
    get_day = request.POST.get("d")
    get_time = request.POST.get("t")
    get_ticket = request.POST.get("ticket")
    
    
    if request.method == "POST":
        sub = Subscriber(name = name_ , birthday = birthday_)
        sub.save()

        mov = Movie(name = get_movie_name, day = get_day, time = get_time, ticket = get_ticket,  watcher = sub)
        mov.save()
            
        return redirect('done')

    context = {"title":"Booking page"}
    return render(request,'index.html', context=context)

def done(request):
    return render(request,'done.html',{})

def index(request):
    return render(request,'main.html',{})

def dashboard(request):

    if request.method == "POST":
        name = request.POST.get('name')
        birthdate = request.POST.get('birthdate')
        
        movieOne = request.POST.get('fm1')
        if movieOne == 'clicked':
            movie_name = "MovieOne"
        
        movieTwo = request.POST.get('fm2')
        if movieTwo == 'clicked':
            movie_name = "MovieTwo"
        
        timeOne = request.POST.get('ft1')
        if timeOne == 'clicked':
            time = "4-6"
        
        timeTwo = request.POST.get('ft2')
        if timeTwo == 'clicked':
            time = "10-12"
        
        ticket = request.POST.get('ticket')

        sub = Subscriber(name = name , birthday = birthdate)
        sub.save()

        mov = Movie(name = movie_name, time = time, ticket = ticket,  watcher = sub)
        mov.save()
            
        return redirect('done')
        
    return render(request,'dashboard.html',{})