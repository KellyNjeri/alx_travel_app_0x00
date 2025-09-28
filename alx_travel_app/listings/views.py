from rest_framework import generics
from .models import TravelListing
from .serializers import TravelListingSerializer

class TravelListingListCreateView(generics.ListCreateAPIView):
    queryset = TravelListing.objects.all()
    serializer_class = TravelListingSerializer

class TravelListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelListing.objects.all()
    serializer_class = TravelListingSerializer
