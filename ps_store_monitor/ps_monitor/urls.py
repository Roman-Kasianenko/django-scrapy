from django.contrib import admin
from django.urls import path
from .views import GameItemView

urlpatterns = [
    path('', GameItemView.as_view(), name='home'),
]
