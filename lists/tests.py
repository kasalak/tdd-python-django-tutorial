from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item' # first three lines set up
                                                      # test

        response = home_page(request)                 # calls function under test

        self.assertIn('A new list item', response.content.decode()) # test
        expected_html = render_to_string(                           # assertions
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)
        
