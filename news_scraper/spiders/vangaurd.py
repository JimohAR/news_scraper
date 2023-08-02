import scrapy
from news_scraper.utils import *
from datetime import timedelta


class VangaurdSpider(scrapy.Spider):
    name = "vangaurd"
    allowed_domains = ["vanguardngr.com"]
    urls = ["https://www.vanguardngr.com/category/top-stories/"]

    custom_settings = {
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": False,
        }
    }

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url, meta={"playwright": True})

    def parse(self, response):
        end_date = dt.today() - timedelta(days=2)
        end_date_str = self.to_datestr(end_date)

        print(end_date_str, "\n\n\n")
        return

        articles1 = response.xpath(
            '//article[contains(@class,"entry entry-list")]')

        for article in articles1:
            date = article.xpath(
                './/div[@class="entry-date"]/text()').get().strip()
            if date.lower() == end_date_str:
                break
            data = {
                "title": article.xpath('.//h3[@class="entry-title"]/a/text()').get().strip(),
                "link": article.xpath('.//h3[@class="entry-title"]/a/@href').get().strip(),
                "preview": article.xpath('.//p[@class="post-excerpt"]/text()').get().strip(),
                "date": date,
                "photo_link": article.xpath('./a/img/@data-src').get().strip(),
                "outlet": "vangaurdngr",
            }

            yield data

        articles2 = response.xpath('//div[@class="just-in-timeline"]//article')

        for article in articles2:
            date = article.xpath(
                './/div[@class="meta-time"]/span/text()').get().strip()
            if date.lower() == end_date_str:
                return
            data = {
                "title": article.xpath('.//h3[@class="entry-title"]/a/text()').get().strip(),
                "link": article.xpath('.//h3[@class="entry-title"]/a/@href').get().strip(),
                "preview": "",
                "date": date,
                "photo_link": "",
                "outlet": "vangaurdngr",
            }

            yield data

        next_page = response.xpath(
            '//ul[@class="pagination"]/li[last()]/a/@href').get()
        yield response.follow(next_page, callback=self.parse)

    def to_datestr(self, date, months_rep=months_rev):
        new_day = str(date.day)
        new_month = months_rep[f"{date.month:>02}"]

        new_date = f"{new_month} {new_day}, {date.year}"
        return new_date
