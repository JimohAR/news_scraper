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


# class PunchSpider(scrapy.Spider):
#     def __init__(self, days=2, name=None, **kwargs):
#         super().__init__(name, **kwargs)

#         end_date = dt.today() - timedelta(days=days)
#         self.end_date_str = to_datestr(end_date)
