from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField('date of purchase')

    def __str__(self):
        return f'Куплен товар:{self.item.name} -  покупатель:{self.name}, {self.age} лет, дата покупки: {self.date_purchase}'




