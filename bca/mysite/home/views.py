from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contect
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contect = Contect(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contect.save()
        messages.success(request,'Your Message Has Been Sent')
    return render(request,'contect.html')
def service(request):
    return render(request,'service.html')
