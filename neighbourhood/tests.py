from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class LocationTestClass(TestCase):
    def setUp(self):
        self.kasarani = Location(name='Test Location',created_on='12/02/21',updated_on='01/03/2021')

    def test_instance(self):
        self.assertTrue(isinstance(self.kasarani, Location))

    def test_save_method(self):
        self.kasarani.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.kasarani.save_location()
        self.kasarani.delete()
        locations = Location.objects.all()
        self.assertFalse(len(locations) > 0)

    def tearDown(self):
        Location.objects.all().delete()

class PostTestClass(TestCase):
    def setUp(self):
        self.post1 = Post(title='Test Post',description='This a test')

    def test_instance(self):
        self.assertTrue(isinstance(self.post1, Post))

    def test_save_method(self):
        self.post1.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post1.save()
        self.post1.delete_post()
        posts = Post.objects.all()
        self.assertFalse(len(posts) > 0)

    def test_get_post(self):
        user = 1
        post = Post.get_post(user)
        self.assertFalse(len(post)>0)
    
    def tearDown(self):
        Post.objects.all().delete()

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business1 = Business(business_name='Test Business',business_logo='logo.png',business_contact='test@test.com',created_at='12/05/21')

    def test_instance(self):
        self.assertTrue(isinstance(self.business1, Business))

    def test_create_method(self):
        self.business1.save()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business1.save()
        self.business1.delete_business()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)

    def tearDown(self):
        Business.objects.all().delete()

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.hood1 = Neighbourhood(hood_name='Test Business',hood_image='logo.png',help_line='test@test.com',created_on='12/05/21',updated_on='03/05/21',description='Test hood init',resident_count='2')

    def test_instance(self):
        self.assertTrue(isinstance(self.hood1, Neighbourhood))

    def test_create_method(self):
        self.hood1.save()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)
    
    def test_delete_method(self):
        self.hood1.save()
        self.hood1.delete_neighbourhood()
        businesses = Business.objects.all()
        self.assertFalse(len(businesses) > 0)