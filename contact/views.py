from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Message
from django.contrib import messages

from django.contrib.auth import authenticate , login , logout


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request , 'contact/index.html')
    else:
        return render(request , 'contact/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect('contact:contacto')
    
    return render(request , 'contact/index.html')

def contact(request):
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        message = request.POST['message']
        new_message =Message(first=first, last=last, email=email , message=message)
        new_message.save()
        messages.success(request, 'لقد تم إستقبال رسالتكم بنجاح')
        
        return redirect('contact:contacto')
    
    # introducing 
    users = User.objects.all()
    
    mymessages = Message.objects.all().order_by('-id')
    
    context = {'mymessages':mymessages , 'users':users}
    
    
    return render(request, 'contact/contact.html' , context)

