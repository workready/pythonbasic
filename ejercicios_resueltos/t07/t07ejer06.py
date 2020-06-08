import calendar
from pprint import pprint

months = [n for n in calendar.month_name[1:]]
days_per_month = [calendar.monthrange(2016, index + 1)[1] for index, month in enumerate(months)]

pprint(dict(zip(months, days_per_month)))