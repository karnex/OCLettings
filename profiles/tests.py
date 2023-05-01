from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from profiles.models import Profile

import re


class TestProfiles(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='4meRomance', password='@1QwhjlL_nf387f')
        self.profile = Profile.objects.create(favorite_city='Barcelona', user=self.user)

    def test_profile_list(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, '<h1>Profiles</h1>')

    def test_profile_detail(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        title = re.search("<title>(.*)</title>", response.content.decode('utf-8')).group(1)
        self.assertContains(response, f'<h1>{title}</h1>')
