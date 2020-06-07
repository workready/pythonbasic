import json, requests
import pprint


def _get_base_url():
    return 'http://restcountries.eu/rest/v2/name/'

def _get_country_data(country):
    base_url = _get_base_url()

    url = "{}/{}".format(base_url, country)

    resp = requests.get(url=url)

    return resp

def parse_data(resp):
    data = json.loads(resp.text)
    return data

def get_capital(country):
    country_data = _get_country_data(country)

    country_data_json = parse_data(country_data)
    return country_data_json["capital"]

def get_population(country):
    country_data = _get_country_data(country)

    country_data_json = parse_data(country_data)
    return country_data_json["population"]

def get_timezones(country):
    country_data = _get_country_data(country)

    country_data_json = parse_data(country_data)
    return country_data_json["time_zones"]
