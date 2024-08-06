# Trip Management FastAPI Service

## Overview

This FastAPI microservice provides endpoints to create, list, modify, and delete trips. A trip consists of information about a vacation, including destination, start date, end date, and an optional description.

## Features

- Create a new trip.
- List all trips.
- Retrieve a specific trip by ID.
- Update a specific trip by ID.
- Delete a specific trip by ID.

## Endpoints

### Create Trip

- **Endpoint**: `/trips`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "destination": "string",
    "start_date": "string",
    "end_date": "string",
    "description": "string"
  }
  ```
- **Response**:
  - `200 OK`: Returns the created trip.
  ```json
  {
    "id": "uuid",
    "destination": "string",
    "start_date": "string",
    "end_date": "string",
    "description": "string"
  }
  ```

### List Trips

- **Endpoint**: `/trips`
- **Method**: `GET`
- **Response**:
  - `200 OK`: Returns a list of all trips.
  ```json
  [
    {
      "id": "uuid",
      "destination": "string",
      "start_date": "string",
      "end_date": "string",
      "description": "string"
    }
  ]
  ```

### Get Trip by ID

- **Endpoint**: `/trips/{trip_id}`
- **Method**: `GET`
- **Path Parameters**:
  - `trip_id`: The ID of the trip to retrieve.
- **Response**:
  - `200 OK`: Returns the specified trip.
  ```json
  {
    "id": "uuid",
    "destination": "string",
    "start_date": "string",
    "end_date": "string",
    "description": "string"
  }
  ```
  - `404 Not Found`: If the specified trip does not exist.
  ```json
  {
    "detail": "Trip not found"
  }
  ```

### Update Trip

- **Endpoint**: `/trips/{trip_id}`
- **Method**: `PUT`
- **Path Parameters**:
  - `trip_id`: The ID of the trip to update.
- **Request Body**:
  ```json
  {
    "destination": "string",
    "start_date": "string",
    "end_date": "string",
    "description": "string"
  }
  ```
- **Response**:
  - `200 OK`: Returns the updated trip.
  ```json
  {
    "id": "uuid",
    "destination": "string",
    "start_date": "string",
    "end_date": "string",
    "description": "string"
  }
  ```
  - `404 Not Found`: If the specified trip does not exist.
  ```json
  {
    "detail": "Trip not found"
  }
  ```

### Delete Trip

- **Endpoint**: `/trips/{trip_id}`
- **Method**: `DELETE`
- **Path Parameters**:
  - `trip_id`: The ID of the trip to delete.
- **Response**:
  - `200 OK`: Returns the deleted trip.
  ```json
  {
    "id": "uuid",
    "destination": "string",
    "start_date": "string",
    "end_date": "string",
    "description": "string"
  }
  ```
  - `404 Not Found`: If the specified trip does not exist.
  ```json
  {
    "detail": "Trip not found"
  }
  ```

## Running the Service

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies:
    ```bash
    pip install fastapi uvicorn
    ```

### Running the Server

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The service will be accessible at `http://127.0.0.1:8000`.

## Example Requests

### Create Trip

To create a new trip, send a `POST` request to `/trips`:

```bash
curl -X POST "http://127.0.0.1:8000/trips" -H "Content-Type: application/json" -d '{"destination": "Paris", "start_date": "2024-08-01", "end_date": "2024-08-10", "description": "Vacation in Paris"}'
```

### List Trips

To list all trips, send a `GET` request to `/trips`:

```bash
curl -X GET "http://127.0.0.1:8000/trips"
```

### Get Trip

To get a specific trip by ID, send a `GET` request to `/trips/{trip_id}`:

```bash
curl -X GET "http://127.0.0.1:8000/trips/{trip_id}"
```

### Update Trip

To update a specific trip by ID, send a `PUT` request to `/trips/{trip_id}`:

```bash
curl -X PUT "http://127.0.0.1:8000/trips/{trip_id}" -H "Content-Type: application/json" -d '{"destination": "London", "start_date": "2024-08-05", "end_date": "2024-08-15", "description": "Updated vacation in London"}'
```

### Delete Trip

To delete a specific trip by ID, send a `DELETE` request to `/trips/{trip_id}`:

```bash
curl -X DELETE "http://127.0.0.1:8000/trips/{trip_id}"
```

## Project Structure

```
.
├── app.py        # The main FastAPI application
├── tests.py        # The integration tests
└── README.md      # This README file
```

## Integration Tests

To run the integration tests, ensure you have `pytest` and `httpx` installed:

```bash
pip install pytest httpx
```

Run the tests with:

```bash
pytest tests.py
```

This will run all the tests defined in `tests.py` and provide a report on their success or failure.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [levitesn@oregonstate.edu].
