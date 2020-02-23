from django.test import TestCase
from . models import *

class ProfileTestClass(TestCase):

    def setUp(self):

        self.new_profile=Profile(bio='i love basketball')
    # test for instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))
    # testing the save mothod
    def test_save_profile(self):
        self.new_profile.create_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>0)

class NeighborhoodTestClass(TestCase):

    def setUp(self):
        self.new_neighborhood=Neighborhood(name='killeleshwa',population=20101000)
    def tearDown(self):
        Neighborhood.objects.all().delete()


    # test for instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))
    # test for save method
    def test_save_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood=Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)
    def test_delete_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        self.new_neighborhood.delete_neighborhood()
        neighborhood=Neighborhood.objects.all()
        self.assertEqual(len(neighborhood),0)