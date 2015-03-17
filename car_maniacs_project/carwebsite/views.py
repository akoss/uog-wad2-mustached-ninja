from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    context_dict={}
	
    return render(request, 'carwebsite/index.html', context_dict)
	
def news(request):

    context_dict={}
	 
    return render(request,'carwebsite/news.html', context_dict)
	 

def new_cars(request):
    
	context_dict={}
	
	return render(request, 'carwebsite/new_cars.html', context_dict)
	

def manufacturers(request):
    
	context_dict={}
	
	return render(request, 'carwebsite/manufacturers.html', context_dict)
	
def compare(request):

    context_dict={}
	
    return render(request, 'carwebsite/compare.html', context_dict)
    
def top_rated(request):

    context_dict={}
	
    return render(request, 'carwebsite/top_rated.html', context_dict)
	 

