import countries
import argparse
from pprint import pprint


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("country", help="pais")
    args = parser.parse_args()

    print("Pais: {}".format(args.country))
    print("Capital: {}".format(countries.get_capital(args.country)))
    print("Población: {}".format(countries.get_population(args.country)))
    print("Zonas horarias: {}".format(countries.get_timezones(args.country)))

