from django.db import models

class FoodTruck(models.Model):
    locationid = models.CharField(max_length=100)
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    cnn = models.CharField(max_length=100)
    location_description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    blocklot = models.CharField(max_length=100, null=True, blank=True)
    block = models.CharField(max_length=100, null=True, blank=True)
    lot = models.CharField(max_length=100, null=True, blank=True)
    permit = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100)
    food_items = models.TextField(null=True, blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.TextField(null=True, blank=True)
    dayshours = models.CharField(max_length=255, null=True, blank=True)
    noi_sent = models.CharField(max_length=100, null=True, blank=True)
    approved = models.CharField(max_length=100, null=True, blank=True)
    prior_permit = models.CharField(max_length=100, null=True, blank=True)
    expiration_date = models.CharField(max_length=100, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    fire_prevention_districts = models.CharField(max_length=100, null=True, blank=True)
    police_districts = models.CharField(max_length=100, null=True, blank=True)
    supervisor_districts = models.CharField(max_length=100, null=True, blank=True)
    zip_codes = models.CharField(max_length=100, null=True, blank=True)
    neighborhoods_old = models.CharField(max_length=100, null=True, blank=True)
