import unittest
from unittest import mock
import countries
import json


class TestCountries(unittest.TestCase):

    def setUp(self):
        self.mock_response = mock.Mock()
        self.mock_response.ok = True
        self.mock_response.status_code = 200
        self.mock_response.text = json.dumps([{
            "capital": "Madrid",
            "population": 46438422,
            "timezones": ["UTC", "UTC+01:00"]
        }])


    def test_get_base_url(self):
        self.assertEqual(countries._get_base_url(), 'http://restcountries.eu/rest/v2/name')

    @mock.patch('requests.get')
    def test_get_country_data(self, mock_request):
        mock_request.return_value = self.mock_response
        resp = countries._get_country_data('spain')
        self.assertTrue(resp.ok)
        self.assertEqual(resp.status_code, 200)

    def test_get_unexistent_country_data(self):
        resp = countries._get_country_data('Pritoria')
        self.assertFalse(resp.ok)
        self.assertEqual(resp.status_code, 404)

    @mock.patch('requests.get')
    def test_get_capital(self, mock_request):
        mock_request.return_value = self.mock_response
        resp = countries.get_capital('spain')
        self.assertEqual(resp.title(), 'Madrid')

    @mock.patch('requests.get')
    def test_get_population(self, mock_request):
        mock_request.return_value = self.mock_response
        resp = countries.get_population('spain')
        self.assertIsInstance(resp, int)
        self.assertEqual(resp, 46438422)

    @mock.patch('requests.get')
    def test_get_timezones(self, mock_request):
        mock_request.return_value = self.mock_response
        resp = countries.get_timezones('spain')
        self.assertIsInstance(resp, list)
        self.assertEqual(len(resp), 2)
        self.assertIn("UTC", resp)
        self.assertIn("UTC+01:00", resp)
