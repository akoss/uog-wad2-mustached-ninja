from django.shortcuts import render
from django.http import HttpResponse
from carwebsite.models import Manufacturer,Model,Review,News
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import json

def index(request):
	context_dict={}
	
	# We display news on the front page: 
	news = News.objects.all()
	context_dict["news"] = news
	
	return render(request, 'carwebsite/index.html', context_dict)

def new_cars(request):
	# Getting the top 5 cars by date of release 
    newest_cars = Model.objects.order_by('-dateOfRelease')[:5]
    
    context_dict={'newest':newest_cars}
	
    return render(request, 'carwebsite/new_cars.html', context_dict)
	
	
def compare(request):

    context_dict={}
	
    return render(request, 'carwebsite/compare.html', context_dict)
    
def top_rated(request):
	# Getting the top 5 cars by average ratings 
    favourite_cars = Model.objects.order_by('-averageRatings')[:5]
    
    context_dict={'favourites':favourite_cars}
	
    return render(request, 'carwebsite/top_rated.html', context_dict)

def ethics(request):
	# This is just a simple static ethics statement
    context_dict={}
	 
    return render(request,'carwebsite/ethics-statement.html', context_dict)
	 


def manufacturer(request, manufacturer_name_slug=None):

    context_dict = {}

    try:
        manufacturer = Manufacturer.objects.get(slug=manufacturer_name_slug)
        models = Model.objects.filter(manufacturer=manufacturer).order_by('-averageRatings')
        context_dict['models'] = models
        context_dict['manufacturer'] = manufacturer
    except Manufacturer.DoesNotExist:
        pass


    return render(request, 'carwebsite/manufacturer.html', context_dict)
    
def model(request, manufacturer_name_slug,model_name_slug, rated=False):
    context_dict = {}
    # Rated is passed as True when we're redirected from the rate view. 
    # If rated is True, we display a message that the user has successfully rated the car. 
    
    context_dict["rated"] = rated
      
    try:
        manufacturer = Manufacturer.objects.get(slug=manufacturer_name_slug)
        model=Model.objects.get(slug=model_name_slug)
        if model.manufacturer==manufacturer:
            context_dict['model']=model
        context_dict['manufacturer'] = manufacturer
    except:
        pass

    return render(request, 'carwebsite/model.html', context_dict)

def compare(request, manufacturer1_name_slug=None,manufacturer2_name_slug=None,model1_name_slug=None,model2_name_slug=None):
    context_dict = {}
    
    # We need two manufacturers and two models  
    try:
        manufacturer1 = Manufacturer.objects.get(slug=manufacturer1_name_slug)
        model1=Model.objects.get(slug=model1_name_slug)
        if model1.manufacturer==manufacturer1:
            context_dict['model1']=model1
        context_dict['manufacturer1'] = manufacturer1
    except:
        pass

    try:
        manufacturer2 = Manufacturer.objects.get(slug=manufacturer2_name_slug)
        model2=Model.objects.get(slug=model2_name_slug)
        if model2.manufacturer==manufacturer2:
            context_dict['model2']=model2
        context_dict['manufacturer2'] = manufacturer2
    except:
        pass


    return render(request, 'carwebsite/compare.html', context_dict)


@login_required
def rate(request, manufacturer_name_slug,model_name_slug):
    context_dict = {}
    # Preparing context dict
    try:
        manufacturer = Manufacturer.objects.get(slug=manufacturer_name_slug)
        model=Model.objects.get(slug=model_name_slug)
        if model.manufacturer==manufacturer:
            context_dict['model']=model
        context_dict['manufacturer'] = manufacturer
    except:
        pass
	 
	# If a review's being posted: 
    if request.method == 'POST':
    	def validate(value): 
    		return (int(value) > 0 and int(value) <= 10)

    	# We check it
    	if validate(request.POST["acceleration"]) and validate(request.POST["speed"]) and validate(request.POST["handling"]) and validate(request.POST["security"]):
			# I put the thing down
			print "Posting review as acceleration: " + str(int(float(request.POST["acceleration"]))) + ", speed: " + str(int(float(request.POST["speed"]))) + ", handling: " + str(int(float(request.POST["handling"]))) + ", security: " + str(int(float(request.POST["security"])))
			review = Review.create(reviewer=request.user, model=model, speed=int(float(request.POST["speed"])), acceleration=int(float(request.POST["acceleration"])), handling=int(float(request.POST["handling"])), security=int(float(request.POST["security"])))
			# Flip it then reverse it. 
			# I mean I save it. 
			review.save()
			# Also, we return to the previous page with a special message. 
			context_dict["rated"] = True    
			return redirect('model', manufacturer_name_slug=manufacturer.slug,model_name_slug=model.slug, rated=True)
    	else: 
    		# If a review's being posted but the data are incorrect, we display a warning. 
    		context_dict["again"] = True
	        return render(request, 'carwebsite/rate.html', context_dict)
    else:
    	# If a review's not being posted we serve the actual form. 
    	context_dict["rated"] = False
    	context_dict["again"] = False
		
    return render(request, 'carwebsite/rate.html', context_dict)

def get_manufacturers(request): 
	# Returns a JSON with all manufacturers 
	# Used for AJAX requests 
	
	man = Manufacturer.objects.all()
	to_return = [] 
	
	for each in man: 
		to_return.append({"name":each.name,"slug":each.slug}) 
	
	return HttpResponse(json.dumps(to_return), content_type="application/json")

def get_models(request,manufacturer_name_slug): 
	# Returns a JSON with models of a specific manufacturer 
	# Used for AJAX requests
	to_return = [] 

	try:
		manufacturer = Manufacturer.objects.get(slug=manufacturer_name_slug)
		models = Model.objects.filter(manufacturer=manufacturer).order_by('title')
	
		for each in models: 
			to_return.append({"title":each.title,"slug":each.slug}) 
	
	except:
		pass
	
	return HttpResponse(json.dumps(to_return), content_type="application/json")

def search(request):
    context_dict = {}
    q = request.POST['query'].strip()
        
    
    results = Model.objects.filter(Q(manufacturer__name__icontains=q)| Q(title__icontains = q))

    context_dict['results']=results
 
    return render(request, 'carwebsite/results.html',context_dict)


