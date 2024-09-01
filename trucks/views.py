import csv
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from geopy.distance import geodesic


@api_view(['POST'])
def load_csv_from_path(request):
    file_path = request.data.get('file_path')

    if not file_path:
        return JsonResponse({'error': 'No file path provided'}, status=400)

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    latitude = float(row['Latitude'])
                    longitude = float(row['Longitude'])

                    # Provide a default value if x or y is missing
                    # x = float(row['X']) if row['X'] else 0.0
                    # y = float(row['Y']) if row['Y'] else 0.0

                    FoodTruck.objects.create(
                        locationid=row['locationid'],
                        applicant=row['Applicant'],
                        facility_type=row['FacilityType'],
                        cnn=row['cnn'],
                        location_description=row['LocationDescription'],
                        address=row['Address'],
                        blocklot=row['blocklot'],
                        block=row['block'],
                        lot=row['lot'],
                        permit=row['permit'],
                        status=row['Status'],
                        food_items=row['FoodItems'],
                        x=row['X'],
                        y=row['Y'],
                        latitude=latitude,
                        longitude=longitude,
                        schedule=row['Schedule'],
                        dayshours=row['dayshours'],
                        noi_sent=row['NOISent'],
                        approved=row['Approved'],
                        prior_permit=row['PriorPermit'],
                        expiration_date=row['ExpirationDate'],
                        location=row['Location'],
                        fire_prevention_districts=row['Fire Prevention Districts'],
                        police_districts=row['Police Districts'],
                        supervisor_districts=row['Supervisor Districts'],
                        zip_codes=row['Zip Codes'],
                        neighborhoods_old=row['Neighborhoods (old)'],
                    )
                except ValueError:
                    # Skip rows with invalid or missing latitude/longitude
                    continue

        return JsonResponse({'status': 'Data loaded successfully'})
    
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def nearby_food_trucks(request):
    lat = float(request.query_params.get('lat'))
    lon = float(request.query_params.get('lon'))
    user_location = (lat, lon)

    # Get all food trucks
    trucks = FoodTruck.objects.all()

    # Calculate distance for each truck
    for truck in trucks:
        truck_distance = geodesic(user_location, (truck.latitude, truck.longitude)).miles
        truck.distance = truck_distance

    # Sort by proximity and limit to 5 results
    nearest_trucks = sorted(trucks, key=lambda x: x.distance)[:5]

    serializer = FoodTruckSerializer(nearest_trucks, many=True)
    return JsonResponse(serializer.data, safe=False)