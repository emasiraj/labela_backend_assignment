from django.db import models

class CarPart(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=10)

    class Meta: 
        ordering = ('name',)

    def __str__(self):
        return self.name

class ShoppingCartItem(models.Model):
    item = models.ForeignKey(CarPart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_sub_total_price(self):
        return self.quantity * self.item.price

    def __str__(self):
        return self.item.name

class Order(models.Model):
    items = models.ManyToManyField(ShoppingCartItem)
    delivery_datetime = models.DateTimeField()
