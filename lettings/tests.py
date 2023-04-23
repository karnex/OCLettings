from django.test import TestCase, Client
from django.urls import reverse

from lettings.models import Letting, Address


class TestLettings(TestCase):

    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(number=7217, street='Bedford Street', city='Brunswick', state='GA',
                                              zip_code=31525, country_iso_code='USA')
        self.letting = Letting.objects.create(title='Joshua Tree Green Haus /w Hot Tub', address=self.address)

    def test_letting_list(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_detail(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
