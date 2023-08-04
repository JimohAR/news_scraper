# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
# from scrapy.exceptions import DropItem

import sqlite3
# from sqlite3 import Error

from queries import insert_news, remove_duplicates


class NewsScraperPipeline:
    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, None)

        return item


class SQLitePipeline:
    collection_name = "scrapy_items"

    def __init__(self, sqlite_uri):
        self.sqlite_uri = sqlite_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlite_uri=crawler.settings.get("SQLITE_URI"),
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_uri)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        # remove duplicates
        self.cursor.execute(remove_duplicates)
        self.conn.commit()

        # close spider
        self.conn.close()

    def process_item(self, item, spider):
        # insert news post into database
        i = ItemAdapter(item).asdict()

        # (title, link, preview, date, photo_link, outlet)
        data = (i.get("title"), i.get("link"), i.get("preview"),
                i.get("date"), i.get("photo_link"), i.get("outlet"))

        self.cursor.execute(insert_news, data)
        self.conn.commit()
        return item


# TODO: Implement a better duplicate filter:
#   load the last n days of data from database
#   use it to determine new duplicates and remove them
#   this will reduce the load on the database, (as if we have 10 million rows ^()^ )

# class DuplicatesPipeline:
#     def __init__(self):
#         self.links_seen = set()

#     def process_item(self, item, spider):
#         adapter = ItemAdapter(item)
#         if adapter["link"] in self.links_seen:
#             raise DropItem(f"Duplicate item found: {item!r}")
#         else:
#             self.links_seen.add(adapter["link"])
#             return item
