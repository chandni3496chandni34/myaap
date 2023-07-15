from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    messages.success(request,"this is test message")
    return render(request,'index.html')
    #return HttpResponse("this ishomepage")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this isaboutpage")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is service gold page")
def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        text=request.POST.get('text')
        
        contact=Contact(email=email,text=text)
        contact.save()
        messages.success(request, "your response sumitted.")
       
        
    return render(request,'contact.html')
    # return HttpResponse("this is contact page")