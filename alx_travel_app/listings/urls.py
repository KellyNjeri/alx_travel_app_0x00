from django.urls import path
from .views import TravelListingListCreateView, TravelListingDetailView

urlpatterns = [
    path('', TravelListingListCreateView.as_view(), name='listings-list-create'),
    path('<int:pk>/', TravelListingDetailView.as_view(), name='listings-detail'),
]
