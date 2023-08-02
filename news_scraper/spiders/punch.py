import scrapy
from news_scraper.utils import *
from datetime import timedelta


class PunchSpider(scrapy.Spider):
    name = "punch"
    allowed_domains = ["punchng.com"]
    start_urls = ["https://punchng.com/topics/news/"]

    def parse(self, response):
        end_date = dt.today() - timedelta(days=2)

        articles1 = response.xpath(
            '//div[@class="latest-news-timeline-section"]/article')

        for article in articles1:
            date = article.xpath(
                './/span[@class="post-date"]/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                break
            else:
                date_iso = dt_date.date().isoformat()

            data = {
                "title": article.xpath('.//h1[@class="post-title"]/a/text()').get().strip(),
                "link": article.xpath('.//h1[@class="post-title"]/a/@href').get().strip(),
                "preview": article.xpath('.//p[@class="post-excerpt"]/text()').get().strip(),
                "date": date_iso,
                "photo_link": str(article.xpath('./a/img/@data-src').get()).strip(),
                "outlet": "punchng",
            }

            yield data

        articles2 = response.xpath('//div[@class="just-in-timeline"]//article')

        for article in articles2:
            date = article.xpath(
                './/div[@class="meta-time"]/span/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                return
            else:
                date_iso = dt_date.date().isoformat()

            data = {
                "title": article.xpath('.//h3[@class="entry-title"]/a/text()').get().strip(),
                "link": article.xpath('.//h3[@class="entry-title"]/a/@href').get().strip(),
                "preview": "",
                "date": date_iso,
                "photo_link": "",
                "outlet": "punchng",
            }

            yield data

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
