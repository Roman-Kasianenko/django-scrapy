from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from ps_monitor.models import GameItem, UrlItem


class GameItemView(ListView):
    model = GameItem
    slug_field = "name"
    template_name = "ps_monitor/gameitem_detail.html"

    def get_queryset(self):
        queryset = GameItem.objects.filter(url_item__in=UrlItem.objects.filter(user=self.request.user))\
            .filter(name=self.kwargs['slug']).order_by('-updated_at')
        return queryset


class GameItemListView(LoginRequiredMixin, ListView):
    model = GameItem
    queryset = GameItem.objects.all()
    template_name = 'ps_monitor/home.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        urls = UrlItem.objects.filter(user=self.request.user)
        items = []
        for url in urls:
            gameitem = GameItem.objects.filter(url_item=url).order_by('-updated_at').first()
            items.append(gameitem)

        context['items'] = items
        return context


class GameItemNewlyAddedListView(ListView):
    model = GameItem
    queryset = GameItem.objects.filter()
    template_name = 'ps_monitor/newly_added.html'


class GameItemCreate(CreateView):
    model = UrlItem
    fields = ['name', 'url']
    success_url = reverse_lazy('ps_monitor:newly_added')

    def form_valid(self, form):
        self.item = form.save(commit=False)
        self.item.user = self.request.user
        self.item.save()
        return redirect('ps_monitor:home')


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