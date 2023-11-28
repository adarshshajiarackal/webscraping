from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse
from webapp.models import link
# Create your views here.
def index(request):
    if request.method == 'POST':
        url1=request.POST.get('url')
        url=requests.get(url1)
        beautifulsoup=BeautifulSoup(url.text,'html.parser')
        address=[]
        for li in beautifulsoup.find_all('a'):
            address=li.get('href')
            stringdata=li.string
            link.objects.create(links=address,string=stringdata)
        return redirect('index')
    address_data=link.objects.all()
    return render(request, 'index.html',{'address_data':address_data})