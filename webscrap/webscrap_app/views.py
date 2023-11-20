from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from . models import Link

# Create your views here.
def index(request):
    if request.method=="POST":
        link_new=request.POST.get('name','')
        urls=requests.get("https://getbootstrap.com/")
        soup=BeautifulSoup(urls.text,"html.parser")

        for link in soup.find_all('a'):
            link_name=link.string
            link_address=link.get('href')
            Link.objects.create(name=link_name,address=link_address)
        return HttpResponseRedirect('/')
    else:
        values=Link.objects.all()
    return render(request,'index.html',{'values':values})
    
