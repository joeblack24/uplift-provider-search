from django.test import TestCase, RequestFactory, Client
from .models import Provider
from django.urls import reverse
import json

class ProviderTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Provider.objects.create(id=1, first_name='Joe', last_name='Blackwell', language='Engish', primary_skills=['Coding', 'Testing', 'Python'], secondary_skill=['Football', 'Madden', 'Video Games'], rating=8.9, active=True)
        Provider.objects.create(id=2, first_name='Jamie', last_name='Foxx', language='Spanish', primary_skills=['Singing', 'Acting', 'Comedy'], secondary_skill=['Football', 'Soccer', 'Jingles'], rating=6.7, active=True)
        Provider.objects.create(id=3, first_name='Fancy', last_name='Clips', language='Hatian', primary_skills=['Business', 'Hospitality'], secondary_skill=['Acting', 'Dancing', 'Fashion'], rating=8.4, active=False)

    def test_skill_filter(self):
        response = self.client.post(reverse('provider_list'),{'skills': ['Python', 'Hospitality']})
        response_json = json.loads(response.content)
        self.assertEquals(2, len(response_json))

    def test_name_filter(self):
        response = self.client.post('/provider_filter',{'name': 'Jamie'})
        response_json = json.loads(response.body)
        self.assertEquals(1, len(response_json))

    def test_language_filter(self):
        response = self.client.post('/provider_filter',{'language': 'Spanish'})
        response_json = json.loads(response.body)
        self.assertEquals(2, len(response_json))
