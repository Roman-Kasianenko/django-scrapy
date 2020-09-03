from ps_monitor.models import GameItem

class CrawlerPipeline:
    def process_item(self, item, spider):
        pk = item['pk']
        gameitem = GameItem.objects.filter(pk=pk).first()
        gameitem.name = item['name']
        gameitem.description = item['description']
        gameitem.old_price = item['old_price']
        gameitem.price = item['price']
        gameitem.game_image_url = item['game_image_url']
        gameitem.discount_value = item['discount_value']
        gameitem.newly_added = False
        gameitem.save()
        return item
