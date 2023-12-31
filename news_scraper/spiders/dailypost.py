from datetime import timedelta

import scrapy
from scrapy.loader import ItemLoader

from news_scraper.utils import *
from news_scraper.spiders.base import *


class DailypostSpider(BaseSpider):
    name = "dailypost"
    allowed_domains = ["dailypost.ng"]
    start_urls = ["https://dailypost.ng/hot-news/"]

    def parse(self, response, page=1):
        end_date = self.end_date

        articles2 = response.xpath(
            '//div[contains(@class, "mvp-widget-feat2-right-main")]/a')
        for article in articles2:
            l = ItemLoader(item=NewsScraperItem(), selector=article)

            date = article.xpath(
                './/span[contains(@class,"mvp-cd-date left relative")]/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                break
            else:
                date_iso = dt_date.date().isoformat()

            l.add_xpath(
                "title", './/div[contains(@class, "mvp-widget-feat2-right-text")]/h2')
            l.add_xpath("link", './@href')
            # l.add_xpath("preview", '')
            l.add_value("date", date_iso)
            l.add_xpath("photo_link", './/img/@src')
            l.add_value("outlet", 'dailypostng')

            yield l.load_item()

        articles1 = response.xpath(
            '//ul[contains(@class, "mvp-blog-story-list left")]/li')

        for article in articles1:
            l = ItemLoader(item=NewsScraperItem(), selector=article)

            date = article.xpath(
                './/span[contains(@class,"mvp-cd-date")]/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                return
            else:
                date_iso = dt_date.date().isoformat()

            l.add_xpath(
                "title", './/div[contains(@class,"mvp-blog-story-text")]/h2')
            l.add_xpath("link", './a/@href')
            l.add_xpath(
                "preview", './/div[contains(@class,"mvp-blog-story-text")]/p')
            l.add_value("date", date_iso)
            l.add_xpath(
                "photo_link", './/img[contains(@class,"mvp-reg-img")]/@src')
            l.add_value("outlet", 'dailypostng')

            yield l.load_item()

        next_page = self.start_urls[0] + f"page/{page+1}/"
        yield response.follow(next_page, callback=self.parse, cb_kwargs={"page": page+1})

    def to_datetime(self, date):
        dsplit = date.split()
        freq = int(dsplit[0])
        period = dsplit[1]
        period_dict = {}

        if period in "secs":
            period_dict = {"seconds": freq}
        elif period in "mins":
            period_dict = {"minutes": freq}
        elif period in "hours":
            period_dict = {"hours": freq}
        elif period in "days":
            period_dict = {"days": freq}
        elif period in "weeks":
            period_dict = {"days": freq * 7}

        new_date = dt.today() - timedelta(**period_dict)

        return new_date
