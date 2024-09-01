from django.urls import path
from . import views

urlpatterns = [
    path('api/foodtrucks/', views.nearby_food_trucks),
    path('api/loadcsv/', views.load_csv_from_path),
]
