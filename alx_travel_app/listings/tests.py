from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Listing

class ListingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.listing = Listing.objects.create(
            title="Test Hotel",
            description="Nice place",
            location="Nairobi",
            price="100.00",
        )

    def test_list_listings(self):
        url = reverse("listing-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.json()) >= 1)

    def test_create_listing(self):
        url = reverse("listing-list")
        data = {
            "title": "New Stay",
            "description": "Cozy room",
            "location": "Mombasa",
            "price": "150.50",
        }
        resp = self.client.post(url, data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
