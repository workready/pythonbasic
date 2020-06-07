import unittest
import countries


class TestCountries(unittest.TestCase):

    def test_get_base_url(self):
        self.assertEqual(countries._get_base_url(), 'http://restcountries.eu/rest/v2/name')

    def test_get_country_data(self):
        resp = countries._get_country_data('spain')
        self.assertTrue(resp.ok)
        self.assertEqual(resp.status_code, 200)

    def test_get_unexistent_country_data(self):
        resp = countries._get_country_data('Pritoria')
        self.assertFalse(resp.ok)
        self.assertEqual(resp.status_code, 404)

    def test_get_capital(self):
        resp = countries.get_capital('spain')
        self.assertEqual(resp.title(), 'Madrid')

    def test_get_population(self):
        resp = countries.get_population('spain')
        self.assertIsInstance(resp, int)
        self.assertEqual(resp, 46438422)

    def test_get_timezones(self):
        resp = countries.get_timezones('spain')
        self.assertIsInstance(resp, list)
        self.assertEqual(len(resp), 2)
        self.assertIn("UTC", resp)
        self.assertIn("UTC+01:00", resp)
