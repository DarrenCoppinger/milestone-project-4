from django.db import models
from products.models import Product

class Order(models.Model):
    STOOL_1 = "1"
    STOOL_2 = "2"
    STOOL_3 = "3"
    STOOL_4 = "4"
    STOOL_5 = "5"
    WINDOW_1 = "6"
    WINDOW_2 = "7"
    WINDOW_3 = "8"
    WINDOW_4 = "9"
    WINDOW_5 = "10"
    BOOTH_1 = "11"
    BOOTH_2 = "12"
    BOOTH_3 = "13"
    BOOTH_4 = "14"
    BOOTH_5 = "15"
    TABLE_1 = "16"
    TABLE_2 = "17"
    TABLE_3 = "18"
    TABLE_4 = "19"
    TABLE_5 = "20"
    TABLE_CHOICE = (
        (STOOL_1, 'Stool No.1'),
        (STOOL_2, 'Stool No.2'),
        (STOOL_3, 'Stool No.3'),
        (STOOL_4, 'Stool No.4'),
        (STOOL_5, 'Stool No.5'),
        (WINDOW_1, 'Window No.1'),
        (WINDOW_2, 'Window No.2'),
        (WINDOW_3, 'Window No.3'),
        (WINDOW_4, 'Window No.4'),
        (WINDOW_5, 'Window No.5'),
        (BOOTH_1, 'Booth No.1'),
        (BOOTH_2, 'Booth No.2'),
        (BOOTH_3, 'Booth No.3'),
        (BOOTH_4, 'Booth No.4'),
        (BOOTH_5, 'Booth No.5'),
        (TABLE_1, 'Table No.1'),
        (TABLE_2, 'Table No.2'),
        (TABLE_3, 'Table No.3'),
        (TABLE_4, 'Table No.4'),
        (TABLE_5, 'Table No.5'),
    )
    table_number = models.SmallIntegerField(
        choices=TABLE_CHOICE,
        default=STOOL_1)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(
            self.table_number,
            self.full_name,
            self.date)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity,
            self.product.name,
            self.product.price)
