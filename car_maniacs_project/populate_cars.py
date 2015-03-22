import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_maniacs_project.settings')

import django
django.setup()

from carwebsite.models import Manufacturer, Model
from datetime import *


def populate():
    toyota = add_manu(name='Toyota',
        image="static/images/Toyota.jpg")

    add_model(manu=toyota,
        title="Corolla",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2015-03-14",
        price="11000",
        picture="static/images/Corolla.jpg")

    add_model(manu=toyota,
        title="Yaris",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2012-11-11",
        price="9000",
        picture="static/images/Yaris.jpg")

    add_model(manu=toyota,
        title="Fortuner",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2010-03-16",
        price="15000",
        picture="static/images/Fortuner.jpg")

    honda = add_manu(name='Honda',
        image="static/images/Honda.jpg")

    add_model(manu=honda,
        title="Civic",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2007-06-29",
        price="8000",
        picture="static/images/Civic.jpg")

    add_model(manu=honda,
        title="Accord",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2011-01-01",
        price="12000",
        picture="static/images/Accord.jpg")

    hyundai = add_manu(name='Hyundai',
        image="static/images/Hyundai.jpg")

    add_model(manu=hyundai,
        title="Accent",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2012-03-14",
        price="14000",
        picture="static/images/Accent.jpg")
        
    renault = add_manu(name='Renault',
        image="static/images/Renault.jpg")
        
    add_model(manu=renault,
        title="Megane",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2008-05-04",
        price="16000",
        picture="static/images/Megane.jpg")
        
    add_model(manu=renault,
        title="Clio",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2010-06-20",
        price="15000",
        picture="static/images/Clio.jpg")
        
    mercedes = add_manu(name='Mercedes-Benz',
        image="static/images/Mercedes.jpg")
    
    add_model(manu=mercedes,
        title="AMG GT",
        speed="0",
        acceleration="0",
        handling="0",
        security="0",
        dateOfRelease= "2015-01-25",
        price="70000",
        picture="static/images/AMG.jpg")
        
        


    # Print out what we have added to the user.
    for manufac in Manufacturer.objects.all():
        for model in Model.objects.filter(manufacturer=manufac):
            print "Added " + manufac.name + " " + model.title

def add_model(manu, title, speed, acceleration, handling, security, dateOfRelease, price,picture):
    model = Model.objects.get_or_create(manufacturer=manu, title=title, speed=speed, acceleration=acceleration,
                                        handling=handling, security=security, dateOfRelease=dateOfRelease,
                                     price=price,picture=picture)[0]
    return model

def add_manu(name,image):
    manufacturer = Manufacturer.objects.get_or_create(name=name,picture=image)[0]
    return manufacturer

# Start execution here!
if __name__ == '__main__':
    print "Starting Car population script..."
    populate()
