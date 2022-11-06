from django.urls import path

from .views import greetings, ListItemView, DetailItemView
    # list_item, detail_item

urlpatterns = [
    path('shop/greetings/', greetings, name='greetings'),
    path('shop/', ListItemView.as_view(), name='list_item'),
    path('shop/<int:pk>/', DetailItemView.as_view(), name='detail_item'),

]