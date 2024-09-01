import csv
from django.core.management.base import BaseCommand
from trucks.models import FoodTruck

class Command(BaseCommand):
    help = 'Load food truck data from CSV file'

    def handle(self, *args, **kwargs):
        with open('C:/Users/pruth/OneDrive/Desktop/Task/Task_F_T/foodtruckfinder/food-truck-data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FoodTruck.objects.create(
                    locationid=row['Locationid'],
                    applicant=row['Applicant'],
                    facility_type=row['FacilityType'],
                    cnn=row['cnn'],
                    location_description=row['LocationDescription'],
                    address=row['Address'],
                    blocklot=row['blocklot'],
                    block=row['block'],
                    lot=row['Lot'],
                    permit=row['permit'],
                    status=row['Status'],
                    food_items=row['FoodItems'],
                    x=float(row['X']),
                    y=float(row['Y']),
                    latitude=float(row['Latitude']),
                    longitude=float(row['Longitude']),
                    schedule=row['Schedule'],
                    dayshours=row['dayshours'],
                    noi_sent=row['NOIsent'],
                    approved=row['Approved'],
                    prior_permit=row['PriorPermit'],
                    expiration_date=row['ExpirationDate'],
                    location=row['Location'],
                    fire_prevention_districts=row['Fire Prevention Districts'],
                    police_districts=row['Police Districts'],
                    supervisor_districts=row['Supervisor Districts'],
                    zip_codes=row['Zip Codes'],
                    neighborhoods_old=row['Neighborhoods(old)'],
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
