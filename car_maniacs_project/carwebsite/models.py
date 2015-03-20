from django.db import models
from django.template.defaultfilters import slugify
#from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    #view = models.IntegerField(default=0)
    #ikes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,max_length=50)

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

#class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
 #   user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    #def __unicode__(self):
        #return self.user.username		
