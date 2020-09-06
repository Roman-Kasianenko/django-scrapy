import scrapy
import re

from ps_monitor.models import UrlItem

try:
    from crawler.items import PsItem
except:
    from crawler.crawler.items import PsItem


class PsSpider(scrapy.Spider):
    name = 'ps'
    allowed_domains = ['store.playstation.com']
    start_urls = ['http://store.playstation.com/']

    def start_requests(self):
        for item in UrlItem.objects.all():
            if item.need_to_monitor:
                yield scrapy.Request(url=item.url, callback=self.parse, meta={'pk': item.id})

    def parse(self, response):
        pk = response.meta['pk']
        current_price = response.css('div.sku-info h3.price-display__price::text').get()
        old_price = response.css('div.sku-info div.price::text').get()

        if not old_price:
            old_price = response.css('div.price-display__price--is-plus-upsell::text').get()

        discount_text = response.css('div.pdp__thumbnail-img span.discount-badge__message::text').get()
        discount = re.sub(r'\D', '', discount_text) if discount_text else 0
        name = response.css('h2.pdp__title::text').get()
        description = response.css('p.pdp__preorder-description ::text').getall()

        if not description:
            description = response.css('div.pdp__description ::text').getall()

        description = ' '.join([d.strip() for d in description if d.strip()])[:450] + '...' if description else description
        game_image_url = response.css('div.pdp__thumbnail-img div.product-image__img--main > img::attr(src)').get()

        item = {}
        item['pk'] = pk
        item['url'] = response.url
        item['name'] = name
        item['description'] = description
        item['game_image_url'] = game_image_url
        item['price'] = self.get_price_value(current_price)
        item['old_price'] = self.get_price_value(old_price)
        item['discount_value'] = float(discount)

        # print(item)
        yield item

    @staticmethod
    def get_price_value(text):
        if text and text.strip():
            price = re.findall(r'(\d+\s?\d+.\d+)', text)
            if price:
                result = re.sub(r'\s', '', price[0])
                return float(result)
        return None
