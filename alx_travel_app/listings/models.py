from django.db import models

class TravelListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    available_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
