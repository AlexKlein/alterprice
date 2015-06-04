from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.abstract_models import NameModel


class CategoryManager(models.Manager):
    def get_list(self):
        return self.all()


class Category(NameModel):
    parent = models.ForeignKey("self",
                               blank=True,
                               null=True,
                               related_name="children")
    click_count = models.IntegerField(default=0,
                                      verbose_name=_('Количество кликов'))
    shop_count = models.IntegerField(default=0,
                                     verbose_name=_('Количество магазинов'))
    goods_count = models.IntegerField(default=0,
                                      verbose_name=_('Количество товаров'))

    objects = CategoryManager()

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
