# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from catalog import views


urlpatterns = patterns(
    '',
    url(r'^$', views.CatalogAllCategoriesPageView.as_view(), name='categories_list'),
    url(r'^(?P<pk>\d+)/$', views.CatalogCategoriesListPageView.as_view(), name='category_categories_list'),
    url(r'^(?P<pk>\d+)/products/$', views.CatalogCategoryProductListPageView.as_view(), name='category_products_list'),
)

