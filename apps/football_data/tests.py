from django.test import TestCase
from django.urls import reverse

from apps.football_data.models import Competition


class IndexTests(TestCase):
    def test_no_urls(self):
        """
        If no URLs exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.context.get('empty_message'), 'There are no URLs in the system yet!')

    def test_get_players(self):
        """
        When submitting an invalid URL, an error is returned to the user
        """

        competition = Competition.objects.create()

        data = {
            'original_url': 'invalid url'
        }

        response = self.client.post(reverse('store'), data=data, follow=True)
        messages = list(response.context.get('messages'))
        self.assertEqual(str(messages[0]), 'Invalid URL')
        self.assertEqual(len(messages), 1)

