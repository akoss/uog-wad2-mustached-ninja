import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_maniacs_project.settings')

import django
django.setup()

from carwebsite.models import Manufacturer, Model
from datetime import *


def populate():
    toyota = add_manu('Toyota')

    add_model(manu=toyota,
        title="Corolla",
        url="http://en.wikipedia.org/wiki/Toyota_Corolla",
        speed="220",
        acceleration="10",
        handling="5",
        security="3",
        #dateOfRelease= datetime.now(),
        price="11000")

    add_model(manu=toyota,
        title="Yaris",
        url="http://en.wikipedia.org/wiki/Toyota_Yaris",
        speed="200",
        acceleration="7",
        handling="4",
        security="2",
       # dateOfRelease= datetime.now(),
        price="9000")

    add_model(manu=toyota,
        title="Fortuner",
        url="http://en.wikipedia.org/wiki/Toyota_Fortuner",
        speed="240",
        acceleration="107",
        handling="5",
        security="5",
       # dateOfRelease= datetime.now(),
        price="15000")

    honda = add_manu('Honda')

    add_model(manu=honda,
        title="Civic",
        url="http://en.wikipedia.org/wiki/Honda_Civic",
        speed="240",
        acceleration="9",
        handling="5",
        security="4",
        #dateOfRelease= datetime.now(),
        price="8000")

    add_model(manu=honda,
        title="Accord",
        url="http://en.wikipedia.org/wiki/Honda_Accord",
        speed="200",
        acceleration="6",
        handling="2",
        security="1",
        #dateOfRelease= datetime.now(),
        price="12000")

    hyundai = add_manu('Hyundai')

    add_model(manu=hyundai,
        title="Accent",
        url="http://en.wikipedia.org/wiki/Hyundai_Accent",
        speed="240",
        acceleration="10",
        handling="5",
        security="3",
       # dateOfRelease= datetime.now(),
        price="14000")


    # Print out what we have added to the user.
    for manu in Manufacturer.objects.all():
        for model in Model.objects.filter(manu=manu):
            print "- {0} - {1}".format(str(c), str(p))

def add_model(manu, title, url, speed, acceleration, handling, security, price):
    model = Model.objects.get_or_create(manufacturer=manu, title=title, url=url, speed=speed, acceleration=acceleration,
                                        handling=handling, security=security,
                                     price=price)[0]
    return model

def add_manu(name):
    manufacturer = Manufacturer.objects.get_or_create(name=name)[0]
    return manufacturer

# Start execution here!
if __name__ == '__main__':
    print "Starting Car population script..."
    populate()
