from django.urls import path
from .views import HousingOfferListView, HousingOfferDetailView, OfferCreateView

urlpatterns = [
    path('', HousingOfferListView.as_view(), name='housing_list'),
    path('housing_details/<int:pk>/', HousingOfferDetailView.as_view(), name='housing_details'),
    path('offer_create/', OfferCreateView.as_view(), name='offer_create'),
]