
# Food Truck Finder API

This is a Django-based API for finding food trucks in San Francisco.

## Installation

1. Clone the repository and navigate to the project directory.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Install `geopy` for calculating distances between coordinates:

```bash
pip install geopy
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
Returns a JSON array of the 5 nearest food trucks, sorted by proximity.
