CarManiacs
==========


An awesome car-rating website
------------------------------


The aim of our website is to help people find a suitable car for their needs. Also, users who own a car cat rate the most important attributes of the car.
We are not promoting car manufacturers, the app is user-centered.  The compare facility helps users pick up a car more suitable for their needs.


Features
-------------------------------

Available for visitors

- View manufacturers and models
- Search bar to easily search for models
- View the newest car on the market
- View the users' favourite cars (top rated)
- Compare (enables viewing 2 cars at the same time)

Exclusive feature

- Rate a car

Instalation instructions
-------------------------

* Clone the repository to your computer


$ git clone https://github.com/akoss/mustached-ninja.git

 
* Create a virtual environment for the app and work on it

$ mkvirtualenv car

$ workon car

* Instal requirements

$ pip install -r requirements.txt

* Run population script and run the server

$ python populate_cars.py

$ python manage.py runserver

* Login

Open your web browser and type in: 127.0.0.1:8000/carwebsite

Login with the following credentials: username=test, password=test

* Enjoy
