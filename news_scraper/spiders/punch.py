from datetime import timedelta

import scrapy
from scrapy.loader import ItemLoader

from news_scraper.utils import *
from news_scraper.items import NewsScraperItem


class PunchSpider(scrapy.Spider):
    name = "punch"
    allowed_domains = ["punchng.com"]
    start_urls = ["https://punchng.com/topics/news/"]

    def parse(self, response):
        end_date = dt.today() - timedelta(days=2)

        articles1 = response.xpath(
            '//div[@class="latest-news-timeline-section"]/article')

        for article in articles1:
            l = ItemLoader(item=NewsScraperItem(), selector=article)

            date = article.xpath(
                './/span[@class="post-date"]/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                break
            else:
                date_iso = dt_date.date().isoformat()

            l.add_xpath("title", './/h1[@class="post-title"]/a')
            l.add_xpath("link", './/h1[@class="post-title"]/a/@href')
            l.add_xpath("preview", './/p[@class="post-excerpt"]')
            l.add_value("date", date_iso)
            l.add_xpath("photo_link", './a/img/@data-src')
            l.add_value("outlet", 'punchng')

            yield l.load_item()

        articles2 = response.xpath('//div[@class="just-in-timeline"]//article')

        for article in articles2:
            l = ItemLoader(item=NewsScraperItem(), selector=article)

            date = article.xpath(
                './/div[@class="meta-time"]/span/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                return
            else:
                date_iso = dt_date.date().isoformat()

            l.add_xpath("title", './/h3[@class="entry-title"]/a')
            l.add_xpath("link", './/h3[@class="entry-title"]/a/@href')
            # l.add_xpath("preview", '')
            l.add_value("date", date_iso)
            # l.add_xpath("photo_link", '')
            l.add_value("outlet", 'punchng')

            yield l.load_item()

        next_page = response.xpath(
            '//ul[@class="pagination"]/li[last()]/a/@href').get()
        yield response.follow(next_page, callback=self.parse)

    def to_datetime(self, date, months_rep=months):
        day, month, year = date.split()
        new_day = ""
        for i in day:
            try:
                new_day += str(int(i))
            except ValueError:
                continue
        new_month = months_rep[month.lower()]

        date = dt.fromisoformat(f"{year}-{new_month}-{new_day:>02}")
        return date
