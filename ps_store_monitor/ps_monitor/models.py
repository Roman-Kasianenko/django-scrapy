from django.db import models
from django.urls import reverse


class GameItem(models.Model):
    url = models.URLField(max_length=200, unique=True, blank=True, null=True)
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", default='')
    game_image_url = models.URLField(max_length=200, blank=True, null=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2, default=0.0)
    old_price = models.DecimalField("Old Price", max_digits=7, decimal_places=2, null=True, blank=True)
    discount_value = models.DecimalField("Discount", max_digits=7, decimal_places=2, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ps_monitor:item_detail", kwargs={"slug": self.name})


class UrlItem(models.Model):
    url = models.URLField(max_length=200)
    name = models.CharField("Name", max_length=100)
    need_to_monitor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.url}'
