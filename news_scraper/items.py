# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def strip(data: str) -> str:
    return data.strip()


kwargs = {
    "input_processor": MapCompose(remove_tags, strip),
    "output_processor": TakeFirst()
}


class NewsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(**kwargs)
    link = scrapy.Field(**kwargs)
    preview = scrapy.Field(**kwargs)
    date = scrapy.Field(**kwargs)
    photo_link = scrapy.Field(**kwargs)
    outlet = scrapy.Field(**kwargs)
