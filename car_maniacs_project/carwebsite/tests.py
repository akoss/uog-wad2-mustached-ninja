from django.test import TestCase, RequestFactory

from carwebsite.models import Manufacturer,Model,News

from django.contrib.auth.models import User, AnonymousUser

from django.core.urlresolvers import reverse

def add_model(manu, title, speed, acceleration, handling, security, dateOfRelease, price):
    model = Model.objects.get_or_create(manufacturer=manu, title=title, speed=speed, acceleration=acceleration,
    handling=handling, security=security, dateOfRelease=dateOfRelease,
    price=price)[0]
    return model

def add_review(reviewer, model, speed, acceleration, handling, security):
    review = Review.objects.get_or_create(reviewer=reviewer, model=model,
    speed=speed, acceleration=acceleration,handling=handling, security=security)[0]
    return review

class ManufacturerMethodTests(TestCase):

    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a manufacturer
        an appropriate slug line is created
        i.e. "Random Manufacturer String" -> "random-manufacturer string"
        """
        manu = Manufacturer(name='Random Manufacturer String')
        manu.save()
        self.assertEqual(manu.slug, 'random-manufacturer-string')


class ModelMethodTests(TestCase):


    def test_ensure_attributes_are_all_right(self):
    
        """
        ensure_attributes_are_all_right checks if atributes are not negative   
        """
        manu = Manufacturer(name='Random Manufacturer String')
        manu.save()
        m=add_model(manu=manu,title='test',speed='-1',acceleration='-2',handling='-10',
        security='-5',dateOfRelease="2011-09-08",price='-50000')

        self.assertEqual((0<=m.speed), True)
        self.assertEqual((0<=m.acceleration), True)
        self.assertEqual((0<=m.handling), True)
        self.assertEqual((0<=m.security), True)
        self.assertEqual((0<=m.price), True)


class NewsMethodTests(TestCase):

    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a news
        an appropriate slug line is created
        i.e. "Random News String" -> "random-news-string"
        """
        news = News(title='Random News String')
        news.save()
        self.assertEqual(news.slug, 'random-news-string')

        
class IndexViewTests(TestCase):

    def setUp(self):
        User.objects.create(username='test',email='test@test.com',password='pass')

    def add_manu(name):
        manu = Manufacturer.objects.get_or_create(name=name)[0]
        return manu

    
    def test_index_view_with_registered_user(self):
        """
        Html should contain 'Hello test!'
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"test")
        
    def test_index_view_with_no_manufacturers(self):
        """
        If no manufacturers exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"There are no manufacturers present")        


    def test_index_view_with_manufacturers(self):
        """
        Test that manufacturers are added and displayed correctly
        """
        manu = Manufacturer(name='test')
        manu.save()
        manu = Manufacturer(name='test2')
        manu.save()        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")
        self.assertContains(response, "test2")
        


class FavouriteViewTests(TestCase):

    def test_favourites_view_with_no_cars(self):
        """
        If no favourites exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('top_rated'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars currently in the database")
        self.assertQuerysetEqual(response.context['favourites'], [])
        

class NewCarsViewTests(TestCase):

    def test_new_cars_view_with_no_cars(self):
        """
        If no new cars exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('new_cars'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cars currently in the database")
        self.assertQuerysetEqual(response.context['newest'], [])


class ManufacturerViewTests(TestCase):

    def test_manufacturer_view_with_no_models(self):
        """
        If no models exist for a manufacturer, an appropriate message should be displayed.
        """
        manu = Manufacturer(name='Test')
        manu.save()        
        response = self.client.get(reverse('manufacturer', args={manu.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No models registered for this manufacturer")
        self.assertQuerysetEqual(response.context['models'], [])

    def test_manufacturer_view_with_no_manufacturers(self):
        """
        If no manufacturers exist, an appropriate message should be displayed.
        """       
        response = self.client.get(reverse('manufacturer'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No manufacturers registered")

