from django.contrib import admin
from django.urls import path
from .views import GameItemView, GameItemCreate, GameItemListView, GameItemNewlyAddedListView, watch_unwatch

urlpatterns = [
    path('', GameItemListView.as_view(), name='home'),
    path('newly', GameItemNewlyAddedListView.as_view(), name='newly_added'),
    path('new', GameItemCreate.as_view(), name='item_new'),
    path("item/<str:slug>/", GameItemView.as_view(), name="item_detail"),
    path("watch_unwatch/<int:pk>/", watch_unwatch, name="watch_unwatch"),
]
