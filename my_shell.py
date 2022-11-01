from shop_main.models import Item, Purchase
from django.utils import timezone


rtx3060 = Item(name="RTX3060", price=700)
rtx3060.save()
rtx2080 = Item(name="RTX2080", price=500)
rtx2080.save()
gtx1660 = Item(name="GTX1660", price=300)
gtx1660.save()
ryzen_7 = Item(name="RYZEN 7", price=150)
ryzen_7.save()
core_i5 = Item(name="Core i5", price=200)
core_i5.save()

Item.objects.all()


p1 = Purchase(name="Almaz", age=21, item=rtx3060, date_purchase=timezone.now())
p1.save()

p2 = Purchase.objects.create(name="Atai", age=24, item=rtx2080, date_purchase=timezone.now())
p3 = Purchase.objects.create(name="Askar", age=18, item=rtx3060, date_purchase=timezone.now())
p4 = Purchase.objects.create(name="Aman", age=24, item=ryzen_7, date_purchase=timezone.now())
p5 = Purchase.objects.create(name="Nursultan", age=28, item=core_i5, date_purchase=timezone.now())
p6 = Purchase.objects.create(name="Pharukh", age=24, item=ryzen_7, date_purchase=timezone.now())
p7 = Purchase.objects.create(name="Veronika", age=24, item=rtx3060, date_purchase=timezone.now())
p8 = Purchase.objects.create(name="Zaebalsov", age=44, item=core_i5, date_purchase=timezone.now())
p9 = Purchase.objects.create(name="Gdetobagov", age=24, item=gtx1660, date_purchase=timezone.now())
p10 = Purchase.objects.create(name="Poshelnahov", age=24, item=rtx3060, date_purchase=timezone.now())

Purchase.objects.all()
