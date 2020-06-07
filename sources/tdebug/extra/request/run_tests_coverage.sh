coverage run --omit=test* --source=. -m unittest test_countries
coverage report -m
coverage html
