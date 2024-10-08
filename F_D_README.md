
# Food Truck Finder API

This is a Django-based API.

## Installation

1. Clone the repository and navigate to the project directory.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## API Endpoints

### 1. Load CSV Data

**URL:** `http://127.0.0.1:8000/api/loadcsv/`  
**Method:** `POST`

**Description:**  
This endpoint loads food truck data from a CSV file into the database.

**Request Body:**  
Pass the file path to the CSV file in the request body as JSON.

```json
{
  "file_path": "C:/Users/pruth/OneDrive/Desktop/Task/Task_F_T/foodtruckfinder/food-truck-data.csv"
}
```

**Response:**  
Returns a status message indicating whether the data was loaded successfully.

### 2. Find Nearby Food Trucks

**URL:** `http://localhost:8000/api/foodtrucks/?lat=37.74574924&lon=-122.3924815`  
**Method:** `GET`

**Description:**  
This endpoint returns the 5 nearest food trucks based on the provided latitude and longitude.

**Query Parameters:**
- `lat`: Latitude of the user's location.
- `lon`: Longitude of the user's location.

**Response:**  
- `status_counts`: A count of food trucks with each status (`SUSPEND`, `APPROVED`, `REQUESTED`, `EXPIRED`, `ISSUED`) among the nearest 5 food trucks.
- `nearest_trucks`: A JSON array of the 5 nearest food trucks, sorted by proximity.

**Example JSON Response:**

```json
{
    "status_counts": {
        "SUSPEND": 0,
        "APPROVED": 3,
        "REQUESTED": 0,
        "EXPIRED": 2,
        "ISSUED": 0
    },
    "nearest_trucks": [
        {
            "id": 10,
            "locationid": "1733610",
            "applicant": "Buenafe",
            "facility_type": "Truck",
            ...
        },
        ...
    ]
}
```
