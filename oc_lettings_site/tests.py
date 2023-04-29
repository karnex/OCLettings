from django.test import TestCase, Client
from django.urls import reverse


class TestIndex(TestCase):

    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
