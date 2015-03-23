from django.test import TestCase

from carwebsite.models import Manufacturer,Model

class ManufacturerMethodTests(TestCase):

    def test_slug_line_creation(self):

        manu = Manufacturer(name='Random Manufacturer String')
        manu.save()
        self.assertEqual(manu.slug, 'random-manufacturer-string')


class ModelMethodTests(TestCase):

    def test_ensure_attributes_are_all_right(self):
    
        """
         ensure_attributes_are_all_right checks if atributes are not negative   
         """
        # manufacturer=Manufacturer(name="name",picture="")
        model=Model(averageRatings=11,speed=-1,acceleration=2,handling=12,security=-5,price=-5)
        self.assertEqual((0<=model.averageRatings<=10), True)
        self.assertEqual((0<=model.speed<=10), True)
        self.assertEqual((0<=model.acceleration<=10), True)
        self.assertEqual((0<=model.handling<=10), True)
        self.assertEqual((0<=model.security<=10), True)
        self.assertEqual((model.price>=0), True)
