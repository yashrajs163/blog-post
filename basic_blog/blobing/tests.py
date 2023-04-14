from django.test import TestCase
from django.urls import resolve , reverse
from .views import home 
from . models import Article 
from blobing.views import details

# Create your tests here.
class HomeTests(TestCase):
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func,home)

class ArticleDetailsTest(TestCase):
    def test_details_view_success_status_code(self):
        url = reverse('details', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


