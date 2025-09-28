from rest_framework import serializers
from .models import TravelListing

class TravelListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelListing
        fields = '__all__'