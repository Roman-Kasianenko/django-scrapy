from django.db import models
from django.urls import reverse


class GameItem(models.Model):
    # item_url = models.SlugField(max_length=160, unique=True, default='')
    url = models.URLField(max_length=200, unique=True, blank=True, null=True)
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", default='')
    game_image_url = models.URLField(max_length=200, blank=True, null=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2, default=0.0)
    old_price = models.DecimalField("Old Price", max_digits=7, decimal_places=2, null=True, blank=True)
    discount_value = models.DecimalField("Discount", max_digits=7, decimal_places=2, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    newly_added = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ps_monitor:item_detail", kwargs={"slug": self.name})



