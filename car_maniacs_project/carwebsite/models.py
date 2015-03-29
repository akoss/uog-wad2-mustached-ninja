from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Manufacturer(models.Model):
	# This model represents car manufacturers. 
	
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True,max_length=50)
    picture = models.ImageField(upload_to='static/images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manufacturer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class News(models.Model):
	# This model represents news that are displayed on the front page. 
	
    title = models.CharField(max_length=256)
    intro = models.CharField(max_length=512)
    link = models.CharField(max_length=256)
    slug = models.SlugField(unique=True,max_length=50)
    picture = models.ImageField(upload_to='static/images', blank=True)
    show = models.BooleanField(default=False)
    # Set show to false to hide the article from the main page. 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # We need to create a slug during saving
        super(News, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Model(models.Model):
	# This model represents car models. 
    picture = models.ImageField(upload_to='static/images', blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    # Each model has got a manufacturer. 
    title = models.CharField(max_length=128,unique=True)
    averageRatings=models.FloatField(default=0.0)
    speed = models.PositiveIntegerField(default=0)
    acceleration = models.PositiveIntegerField(default=0)
    handling = models.PositiveIntegerField(default=0)
    security = models.PositiveIntegerField(default=0)
    # We store the current average rating for each car model inside the model to make the application
    # run faster. These are currently generated each time a new review gets added. 
    
    dateOfRelease = models.DateField()
    price = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True,max_length=50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # We need to create a slug during saving
        super(Model, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Review(models.Model): 
	# This model represents a review submitted by a user. 
	
	reviewer = models.ForeignKey(User, unique=False)
	# User it was submitted by
	model = models.ForeignKey(Model, unique=False)
	# Car model the review is about 
	speed = models.PositiveIntegerField(default=0)
	# We only allow integers here. 
	acceleration = models.PositiveIntegerField(default=0)
	handling = models.PositiveIntegerField(default=0)
	security = models.PositiveIntegerField(default=0)
	
	@classmethod
	def create(cls, reviewer=reviewer, model=model, speed=speed, acceleration=acceleration, handling=handling, security=security): 
		# This is a method to create a review. 
		review = cls()
		review.reviewer = reviewer
		review.model = model 
		review.speed = speed 
		review.acceleration = acceleration
		review.handling = handling
		review.security = security
		return review
    
	def save(self, *args, **kwargs): 
		# If there's already a review from the same person in the database, we delete it 
		reviews = Review.objects.all().filter(reviewer=self.reviewer)
		for each in reviews: 
			each.delete() 
		
		# We save the new record
		super(Review, self).save(*args, **kwargs) 
		
		# And recalculate the new average ratings for the reviewed model
		# Everything under this should be a cron job in the long run
		
		reviews = Review.objects.all().filter(model=self.model)
		speedSum = 0
		accelerationSum = 0
		handlingSum = 0
		securitySum = 0
		
		for each in reviews: 
			speedSum = speedSum + each.speed
			accelerationSum = accelerationSum + each.acceleration
			handlingSum = handlingSum + each.handling
			securitySum = securitySum + each.security
			
		speedSum = speedSum / len(reviews)
		accelerationSum = accelerationSum / len(reviews)
		handlingSum = handlingSum / len(reviews)
		securitySum = securitySum / len(reviews)
		
		# We count the average 
		averageRatings = (speedSum + accelerationSum + handlingSum + securitySum) / 4.0
		
		# We slugify it. 
		model = Model.objects.get(slug=self.model.slug)
		model.averageRatings = averageRatings
		model.speed = speedSum
		model.acceleration = accelerationSum
		model.handling = handlingSum
		model.security = securitySum
		
		# Finally, we save it. 
		model.save()
		
    	
	def __unicode__(self):
		return self.title
