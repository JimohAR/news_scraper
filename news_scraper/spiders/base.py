# import scrapy
# # from news_scraper.utils import *
# from datetime import timedelta

# from datetime import datetime as dt

# months = {
#     "january": "01",
#     "february": "02",
#     "march": "03",
#     "april": "04",
#     "may": "05",
#     "june": "06",
#     "july": "07",
#     "august": "08",
#     "september": "09",
#     "october": "10",
#     "november": "11",
#     "december": "12"
# }

# months_rev = dict(zip(months.values(), months.keys()))

# dayth ={
#     1: "st",
#     21: "st",
#     31: "st",
#     2: "nd",
#     22: "nd",
#     3: "rd",
#     23: "rd"
# }

# dayth.update(zip(list(range(4, 21)), ["th"] * (21-4)))
# dayth.update(zip(list(range(24, 31)), ["th"] * (31-24)))


from datetime import datetime as dt
from datetime import timedelta

import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

from news_scraper.items import NewsScraperItem


class BaseSpider(scrapy.Spider):
    def __init__(self, days=1, name=None, **kwargs):
        super().__init__(name, **kwargs)

        self.end_date = dt.today() - timedelta(days=days)
