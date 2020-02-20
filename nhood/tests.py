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
        self.newhood.deletehood()
        hoods=Neighborhood.objects.all()
        self.assertTrue(len(hoods)==0)
        
    def test_get_hood(self):
        self.newhood.savehood()
        firsthood=Neighborhood.get_hood()
        self.assertTrue(firsthood is not None)
        
class BusinessTestClass(TestCase):
    def setUp(self):
        '''
        Creates and saves user foreign key instance
        '''
        self.newuser=User(username='clover')
        self.newuser.save()
        '''
        Create and saves neighbor foreign key instance
        '''
        self.hood=Neighborhood(hoodpic='pic.jpg',hoodname='SportsDrive',numberofpeople='10',hoodlocation='3rdavenue')
        self.hood.save()
        '''
        Creates and save business foreign key instance
        '''
        self.business=Business(businessname='ngukufarm',businesspic='umg.jpg',businessemail='boss@gmail',editor=self.newuser,area=self.hood)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
        
    def test_save_business(self):
        self.business.savebusiness()
        allbusiness=Business.objects.all()
        self.assertTrue(len(allbusiness)>0)
        
    def test_delete_business(self):
        self.business.savebusiness()
        self.business.deletebusiness()
        allbusiness=Business.objects.all()
        self.assertTrue(len(allbusiness)==0)
        
    def test_get_businesses(self):
        self.business.savebusiness()
        firstbusiness=Business.get_businesses()
        self.assertTrue(firstbusiness is not None )
        
class NewsTestClas(TestCase):
    def setUp(self):
        self.newuser=User(username='clover')
        self.newuser.save()
        self.news=News(title='mandem',newspic='img.jpg',description='blackisbeautiful',editor=self.newuser,newslocation='nairobi')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.news,News))
        
    def test_save_news(self):
        self.news.savenews()
        allnews=News.objects.all()
        self.assertTrue(len(allnews)>0)
        
    def test_delete_news(self):
        self.news.savenews()
        self.news.deletenews()
        allnews=News.objects.all()
        self.assertTrue(len(allnews)==0)
        
    def test_get_new(self):
        self.news.savenews()
        firstnews=News.get_news()
        self.assertTrue(firstnews is not None)