from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #view = models.IntegerField(default=0)
    #ikes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,max_length=50)
    picture = models.ImageField(upload_to='static/images', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manufacturer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
   # class Meta:
   #    verbose_name_plural="Categories";

class Model(models.Model):
    picture = models.ImageField(upload_to='static/images', blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    title = models.CharField(max_length=128,unique=True)
    url = models.URLField()
    #views = models.IntegerField(default=0)
    averageRatings=models.FloatField(default=0.0)
    speed = models.IntegerField(default=0)
    acceleration = models.IntegerField(default=0)
    handling = models.IntegerField(default=0)
    security = models.IntegerField(default=0)
    dateOfRelease = models.DateField()
    price = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,max_length=50)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Model, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Review(models.Model): 
	reviewer = models.ForeignKey(User, unique=False)
	model = models.ForeignKey(Model, unique=False)
	speed = models.IntegerField(default=0)
	acceleration = models.IntegerField(default=0)
	handling = models.IntegerField(default=0)
	security = models.IntegerField(default=0)
	
	@classmethod
	def create(cls, reviewer=reviewer, model=model, speed=speed, acceleration=acceleration, handling=handling, security=security): 
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
		# Everything under this should be a cron job
		
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
		
		averageRatings = (speedSum + accelerationSum + handlingSum + securitySum) / 4.0
		
		model = Model.objects.get(slug=self.model.slug)
		model.averageRatings = averageRatings
		model.speed = speedSum
		model.acceleration = accelerationSum
		model.handling = handlingSum
		model.security = securitySum
		
		model.save()
		
    	
	def __unicode__(self):
		return self.title
	


#class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
 #   user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    #def __unicode__(self):
        #return self.user.username		
