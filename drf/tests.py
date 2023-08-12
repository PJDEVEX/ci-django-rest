from django.test import TestCase
from django.urls import reverse

class LogoutRouteTest(TestCase):

    def test_logout_route_clears_cookies(self):
        url = reverse('logout-route')  # Make sure 'logout-route' is the correct name
        response = self.client.post(url)  # Simulate a POST request to the logout view
        self.assertEqual(response.status_code, 200)  # Assuming a successful logout returns a 200 status code
        # Add assertions to check that cookies are cleared in the response

    def test_logout_route_invalid_method(self):
        url = reverse('logout-route')
        response = self.client.get(url)  # Simulate a GET request to the logout view
        self.assertEqual(response.status_code, 405)  # Expecting a 405 Method Not Allowed status code

    # Add more test methods as needed
