from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.urls import reverse


class Config(models.Model):
    """
    Holder for various config items
    """
    group = models.CharField(max_length=100, blank=False, null=False)
    val_str = models.CharField(max_length=200, blank=True, null=True)
    # val_float = models.Fl
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.group.titla() + '-' + self.val_str.title()


class Screen(models.Model):
    """
    The list object - a container for many items that are related
    Mod 10/22
    """
    number = models.SmallIntegerField(validators=[MinValueValidator(1)], unique=True)
    name = models.CharField(max_length=100, unique=True)
    purpose = models.CharField(max_length=200, blank=False)
    date_first_use = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_destroyed = models.DateTimeField(auto_now=False, auto_now_add=False)
    disabled = models.BooleanField(default=False)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return str(self.number)

