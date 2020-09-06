from ps_monitor.models import GameItem


class CrawlerPipeline:
    def process_item(self, item, spider):
        gameitem = GameItem()
        gameitem.url_item_id = item['pk']
        gameitem.name = item['name']
        gameitem.url = item['url']
        gameitem.description = item['description']
        gameitem.old_price = item['old_price']
        gameitem.price = item['price']
        gameitem.game_image_url = item['game_image_url']
        gameitem.discount_value = item['discount_value']
        gameitem.save()
        return item
