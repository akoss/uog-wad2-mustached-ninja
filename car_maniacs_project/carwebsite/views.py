from django.shortcuts import render
from django.http import HttpResponse
from carwebsite.models import Manufacturer,Model

def index(request):
    
    context_dict={}
	
    return render(request, 'carwebsite/index.html', context_dict)
	
def news(request):

    context_dict={}
	 
    return render(request,'carwebsite/news.html', context_dict)
	 

def new_cars(request):

    newest_cars = Model.objects.order_by('-dateOfRelease')[:5]
    
    context_dict={'newest':newest_cars}
	
    return render(request, 'carwebsite/new_cars.html', context_dict)
	

def manufacturers(request):
    
	context_dict={}
	
	return render(request, 'carwebsite/manufacturers.html', context_dict)
	
def compare(request):

    context_dict={}
	
    return render(request, 'carwebsite/compare.html', context_dict)
    
def top_rated(request):

    favourite_cars = Model.objects.order_by('-averageRatings')[:5]
    
    context_dict={'favourites':favourite_cars}
	
    return render(request, 'carwebsite/top_rated.html', context_dict)
    
def manufacturer(request, manufacturer_name_slug):

    context_dict = {}

    try:
        manufacturer = Manufacturer.objects.get(slug=manufacturer_name_slug)
        context_dict['manufacturer_name'] = manufacturer.name
        models = Model.objects.filter(manufacturer=manufacturer).order_by('-averageRatings')
        context_dict['models'] = models
        context_dict['manufacturer'] = manufacturer
    except Manufacturer.DoesNotExist:
        pass


    return render(request, 'carwebsite/manufacturer.html', context_dict)
    
def model(request, manufacturer_name_slug,model_name_slug):

    context_dict = {}

    try:
        print  manufacturer_name_slug
        manufacturer = Manufacturer.objects.get(slug=manufacturer_name_slug)
        model=Model.objects.get(slug=model_name_slug)
        print  manufacturer_name_slug
        context_dict['manufacturer_name'] = manufacturer.name
        context_dict['model_name']=model.title
        print model.manufacturer
        print manufacturer.name
        if model.manufacturer==manufacturer:
            context_dict['model']=model
            print "abc"
        context_dict['manufacturer'] = manufacturer
    except:
        pass


    return render(request, 'carwebsite/model.html', context_dict)

