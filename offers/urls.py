from django.urls import path
from .views import HousingOfferListView, HousingOfferDetailView, HousingOfferCreateView

urlpatterns = [
    path('', HousingOfferListView.as_view(), name='housing_list'),
    path('housing_details/<int:pk>/', HousingOfferDetailView.as_view(), name='housing_details'),
    path('housing_offer_create/', HousingOfferCreateView.as_view(), name='housing_offer_create'),
]