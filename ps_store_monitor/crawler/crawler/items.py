# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from ps_monitor.models import GameItem
from scrapy_djangoitem import DjangoItem


class PsItem(DjangoItem):
    django_model = GameItem
