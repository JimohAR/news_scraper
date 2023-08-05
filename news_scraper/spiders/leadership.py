from datetime import timedelta

import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

from news_scraper.items import NewsScraperItem
from news_scraper.spiders.base import *


class LeadershipSpider(BaseSpider):
    name = "leadership"
    allowed_domains = ["leadership.ng"]

    url = "https://leadership.ng/nigeria-news/?ajax-request=jnews"

    headers = {
        'authority': 'leadership.ng',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://leadership.ng',
        'referer': 'https://leadership.ng/nigeria-news/',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    payload = "action=jnews_module_ajax_jnews_block_5&module=true&data%5Bfilter%5D=1&data%5Bfilter_type%5D=all&data%5Bcurrent_page%5D={page}&=data%5Battribute%5D%5Bheader_icon%5D%3D&=data%5Battribute%5D%5Bfirst_title%5D%3D&=data%5Battribute%5D%5Bsecond_title%5D%3D&=data%5Battribute%5D%5Burl%5D%3D&=data%5Battribute%5D%5Bheader_background%5D%3D&=data%5Battribute%5D%5Bheader_secondary_background%5D%3D&=data%5Battribute%5D%5Bheader_text_color%5D%3D&=data%5Battribute%5D%5Bheader_line_color%5D%3D&=data%5Battribute%5D%5Bheader_accent_color%5D%3D&=data%5Battribute%5D%5Bheader_filter_category%5D%3D&=data%5Battribute%5D%5Bheader_filter_author%5D%3D&=data%5Battribute%5D%5Bheader_filter_tag%5D%3D&=data%5Battribute%5D%5Binclude_post%5D%3D&=data%5Battribute%5D%5Bexclude_post%5D%3D&=data%5Battribute%5D%5Bexclude_category%5D%3D&=data%5Battribute%5D%5Binclude_author%5D%3D&=data%5Battribute%5D%5Binclude_tag%5D%3D&=data%5Battribute%5D%5Bexclude_tag%5D%3D&=data%5Battribute%5D%5Bforce_normal_image_load%5D%3D&=data%5Battribute%5D%5Bpagination_nextprev_showtext%5D%3D&=data%5Battribute%5D%5Bads_random%5D%3D&=data%5Battribute%5D%5Bads_image%5D%3D&=data%5Battribute%5D%5Bads_image_tablet%5D%3D&=data%5Battribute%5D%5Bads_image_phone%5D%3D&=data%5Battribute%5D%5Bads_image_link%5D%3D&=data%5Battribute%5D%5Bads_image_alt%5D%3D&=data%5Battribute%5D%5Bads_image_new_tab%5D%3D&=data%5Battribute%5D%5Bgoogle_publisher_id%5D%3D&=data%5Battribute%5D%5Bgoogle_slot_id%5D%3D&=data%5Battribute%5D%5Bcontent%5D%3D&=data%5Battribute%5D%5Bads_bottom_text%5D%3D&=data%5Battribute%5D%5Bel_id%5D%3D&=data%5Battribute%5D%5Bel_class%5D%3D&=data%5Battribute%5D%5Bscheme%5D%3D&=data%5Battribute%5D%5Btitle_color%5D%3D&=data%5Battribute%5D%5Baccent_color%5D%3D&=data%5Battribute%5D%5Balt_color%5D%3D&=data%5Battribute%5D%5Bexcerpt_color%5D%3D&=data%5Battribute%5D%5Bcss%5D%3D&data%5Battribute%5D%5Bheader_type%5D=heading_6&data%5Battribute%5D%5Bheader_filter_text%5D=All&data%5Battribute%5D%5Bpost_type%5D=post&data%5Battribute%5D%5Bcontent_type%5D=all&data%5Battribute%5D%5Bsponsor%5D=false&data%5Battribute%5D%5Bnumber_post%5D={size}&data%5Battribute%5D%5Bpost_offset%5D=0&data%5Battribute%5D%5Bunique_content%5D=disable&data%5Battribute%5D%5Bincluded_only%5D=false&data%5Battribute%5D%5Binclude_category%5D=3&data%5Battribute%5D%5Bsort_by%5D=latest&data%5Battribute%5D%5Bdate_format%5D=ago&data%5Battribute%5D%5Bdate_format_custom%5D=Y%2Fm%2Fd&data%5Battribute%5D%5Bexcerpt_length%5D=20&data%5Battribute%5D%5Bexcerpt_ellipsis%5D=...&data%5Battribute%5D%5Bpagination_mode%5D=scrollload&data%5Battribute%5D%5Bpagination_number_post%5D=10&data%5Battribute%5D%5Bpagination_scroll_limit%5D=0&data%5Battribute%5D%5Bads_type%5D=disable&data%5Battribute%5D%5Bads_position%5D=1&data%5Battribute%5D%5Bgoogle_desktop%5D=auto&data%5Battribute%5D%5Bgoogle_tab%5D=auto&data%5Battribute%5D%5Bgoogle_phone%5D=auto&data%5Battribute%5D%5Bboxed%5D=false&data%5Battribute%5D%5Bboxed_shadow%5D=false&data%5Battribute%5D%5Bcolumn_width%5D=auto&data%5Battribute%5D%5Bpaged%5D=1&data%5Battribute%5D%5Bpagination_align%5D=center&data%5Battribute%5D%5Bpagination_navtext%5D=false&data%5Battribute%5D%5Bpagination_pageinfo%5D=false&data%5Battribute%5D%5Bbox_shadow%5D=false&data%5Battribute%5D%5Bpush_archive%5D=true&data%5Battribute%5D%5Bcolumn_class%5D=jeg_col_2o3&data%5Battribute%5D%5Bclass%5D=jnews_block_5"

    def start_requests(self):
        size = 200
        page = 1

        yield scrapy.Request(
            url=self.url, method="POST", headers=self.headers, body=self.payload.format(size=size, page=page), cb_kwargs={"page": page, "size": size}
        )

    def parse(self, response, page, size):
        end_date = self.end_date

        json_response = response.json()
        body = " ".join(json_response["content"].split())

        articles = Selector(text=body).xpath(
            '//article[contains(@class, "jeg_post jeg_pl_lg_2 format")]')

        for article in articles:
            l = ItemLoader(item=NewsScraperItem(), selector=article)

            date = article.xpath(
                './/div[@class="jeg_meta_date"]/a/text()').get().strip()
            dt_date = self.to_datetime(date)

            if end_date >= dt_date:
                return
            else:
                date_iso = dt_date.date().isoformat()

            l.add_xpath(
                "title", './/h3[@class="jeg_post_title"]/a')
            l.add_xpath("link", './/h3[@class="jeg_post_title"]/a/@href')
            l.add_xpath(
                "preview", './/div[@class="jeg_post_excerpt"]/p')
            l.add_value("date", date_iso)
            l.add_xpath(
                "photo_link", './div[@class="jeg_thumb"]/a//img/@data-src')
            l.add_value("outlet", 'leadershipng')

            yield l.load_item()

        next_page = self.url
        yield response.follow(
            next_page, method="POST", callback=self.parse, cb_kwargs={"page": page+1, "size": size}, headers=self.headers, body=self.payload.format(size=size, page=page+1)
        )

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
