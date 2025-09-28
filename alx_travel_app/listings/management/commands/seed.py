from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        # Create a default user if not exists
        user, created = User.objects.get_or_create(username="testuser", defaults={"email": "test@example.com"})

        # Sample data
        listings_data = [
            {"title": "Beach House", "description": "A lovely house by the beach.", "price_per_night": 120.00, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price_per_night": 80.00, "location": "Mt. Kenya"},
            {"title": "City Apartment", "description": "Modern apartment in the city center.", "price_per_night": 150.00, "location": "Nairobi"},
        ]

        for data in listings_data:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Listing '{listing.title}' created"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing '{listing.title}' already exists"))
