from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from ps_monitor.models import GameItem, UrlItem


class GameItemView(DetailView):
    model = GameItem
    slug_field = "name"


class GameItemListView(ListView):
    model = GameItem
    queryset = GameItem.objects.all()
    template_name = 'ps_monitor/home.html'


class GameItemNewlyAddedListView(ListView):
    model = GameItem
    queryset = GameItem.objects.all()
    template_name = 'ps_monitor/newly_added.html'


class GameItemCreate(CreateView):
    model = UrlItem
    fields = ['name', 'url']
    success_url = reverse_lazy('ps_monitor:newly_added')


def watch_unwatch(request, pk):

    # item = GameItem.objects.filter(pk=pk).first()
    # if not item.newly_added:
    #     item.newly_added = not item.newly_added
    #     item.save()

    return redirect('ps_monitor:home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('ps_monitor:home')
    else:
        form = UserCreationForm()
    return render(request, 'ps_monitor/signup.html', {'form': form})