from django.shortcuts import render, HttpResponseRedirect
from .models import Lead


def home(request):
    return render(request, 'home.html', {})


def lead_request(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    message = request.POST.get('message')

    l = Lead.objects.create(name=name, email=email, mobile=mobile, message=message)
    return HttpResponseRedirect("/")