# from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urlresolvers import reverse, resolve


# Create your tests here.
class HomeTest(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)


    def test_home_url_resolves_home_view(self):#this second test function is to make sure django rturns the actual requested url
        view = resolve('/')
        self.assertEquals(view.func, home)