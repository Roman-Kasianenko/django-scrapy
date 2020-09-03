from django.shortcuts import render, redirect

# Create your views here.
#
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from ps_monitor.models import GameItem
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from crawler.crawler.spiders.ps import PsSpider


class GameItemView(DetailView):
    model = GameItem
    slug_field = "name"


class GameItemListView(ListView):
    model = GameItem
    queryset = GameItem.objects.filter(newly_added=False)
    template_name = 'ps_monitor/home.html'


class GameItemNewlyAddedListView(ListView):
    model = GameItem
    queryset = GameItem.objects.filter(newly_added=True)
    template_name = 'ps_monitor/home.html'


class GameItemCreate(CreateView):
    model = GameItem
    fields = ['name', 'url']
    success_url = reverse_lazy('ps_monitor:newly_added')


def watch_unwatch(request, pk):

    item = GameItem.objects.filter(pk=pk).first()
    if not item.newly_added:
        item.newly_added = not item.newly_added
        item.save()

    return redirect('ps_monitor:home')
