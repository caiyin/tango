from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage':"Crunchy,creamy,cookie,candy,cupcake!"}
    return render(request,'rango/index.html',context=context_dict)

def about(request):
	return HttpResponse("Rango says here is about page")
	
# Create your views here.


