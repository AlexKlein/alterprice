from django.core.validators import EMPTY_VALUES
from rest_framework.generics import ListAPIView
from django.db.models import Count
# Project imports
from product import models
from product.api import serializers, filters
from utils.views import APIView


class ProductList(ListAPIView):
    serializer_class = serializers.ProductSerializer
    model = models.Product
    filter_class = filters.ProductListFilter

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.annotate(offers_count=Count('productshop'))
        qs = qs.prefetch_related('productshop_set')
        qs = qs.prefetch_related('productphoto_set')
        return qs


class ProductCount(APIView):
    serializer_class = serializers.ProductCountSerializer

    def success_data(self, serializer):
        response = {}
        price_min = serializer.validated_data.get('price_min', None)
        price_max = serializer.validated_data.get('price_max', None)
        category = serializer.validated_data.get('category')
        brand = serializer.validated_data.get('brand')

        qs = models.Product.objects.get_list()

        if price_min not in EMPTY_VALUES:
            qs = qs.by_min_price(price_min)

        if price_max not in EMPTY_VALUES:
            qs = qs.by_max_price(price_max)

        if len(category) > 0:
            pass
        if len(brand) > 0:
            qs = qs.filter(brand__in=brand)

        response['product_count'] = qs.distinct().count()
        return response


class ProductOffers(ListAPIView):
    serializer_class = serializers.ProductShopSerializer
    model = models.ProductShop
    filter_class = filters.ProductShopFilter

    def get_queryset(self):
        product_id = self.kwargs.get('pk', None)
        qs = self.model.objects.filter(product_id=product_id)
        return qs
