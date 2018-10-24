from djongo import models
from django import forms


class Amount(models.Model):
    state_of_storage = models.FloatField()
    unit_of_measure = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Prices(models.Model):
    gross_price = models.FloatField()
    gross_purchase_price = models.FloatField()
    net_price = models.FloatField()
    vat_value = models.IntegerField()
    excise = models.FloatField()

    class Meta:
        abstract = True


class AdditionalInfo(models.Model):
    product_group = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Product(models.Model):
    symbol = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    amount = models.EmbeddedModelField(
        model_container=Amount
    )
    prices = models.EmbeddedModelField(
        model_container=Prices
    )
    additional_info = models.EmbeddedModelField(
        model_container=AdditionalInfo
    )
    upload_date = models.DateTimeField()
