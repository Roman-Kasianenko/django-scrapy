from django.db import models


class GameItem(models.Model):
    item_url = models.SlugField(max_length=160, unique=True, default='')
    url = models.URLField(max_length=200, unique=True, blank=True, null=True)
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    game_image_url = models.URLField(max_length=200, blank=True, null=True)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2)
    old_price = models.DecimalField("Old Price", max_digits=7, decimal_places=2)
    discount_value = models.DecimalField("Discount", max_digits=7, decimal_places=2)
    updated_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name



