from django.test import TestCase
from .models import Neighborhood,Business,News,UserProfile
from django.contrib.auth.models import User

# Create your tests here.
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.newhood=Neighborhood(hoodpic='pic.jpg',hoodname='SportsDrive',numberofpeople='123',hoodlocation='13thstreet')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.newhood,Neighborhood))
        
    def test_save_hood(self):
        self.newhood.savehood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)>0)
        
    def test_delete_hood(self):
        self.newhood.savehood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)>0)