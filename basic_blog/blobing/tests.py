from django.test import TestCase
from django.urls import resolve
from .views import home 

# Create your tests here.
class HomeTests(TestCase):
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)

        

