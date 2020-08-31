from django.shortcuts import render

# Create your views here.
#
from django.views.generic import ListView

from ps_monitor.models import GameItem


class GameItemView(ListView):
    model = GameItem
    queryset = GameItem.objects.filter()
    # paginate_by = 10
    template_name = 'ps_monitor/home.html'
