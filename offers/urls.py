from django.urls import path
from .views import offers, HouseOfferDetailView, HouseOfferCreateView

urlpatterns = [
    path('', offers),
    path('housing_details/<int:pk>/', HouseOfferDetailView.as_view(), name='housing_details'),
    path('housing_offer_create/', HouseOfferCreateView.as_view(), name='housing_offer_create'),
]