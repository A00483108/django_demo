# Django Hotel API (Assignment)
### Developed By: Sukanta Dey Amit (A00483108)

This is a simple Django project that provides an API for managing hotel data. The project uses Django and Django Rest Framework to handle HTTP requests for hotel information. The API allows users to perform CRUD operations (Create, Read, Update, Delete) on hotel data.

## Features

- API to get a list of hotels (`GET /hotels/`).
- API to add a new hotel (`POST /hotels/`).
- Basic CRUD functionality with Django and Django Rest Framework.
- Supports Hotel data with `name`, `price`, and `available` fields.

## Requirements

- Python 3.8+
- Django 4.0.6+
- Django REST Framework 3.13.1+

## API Endpoints
### 1. Get a List of Hotels
URL: /hotels/

Method: GET

Description: Retrieves a list of all hotels.

Response: A JSON array containing hotel data.

Sample Response:
`[
  {
    "id": 1,
    "name": "Hotel Sunshine",
    "price": 200,
    "available": true
  },
  {
    "id": 2,
    "name": "Grand Plaza",
    "price": 150,
    "available": false
  }
]`

### 2. Create a New Hotel
URL: /hotels/

Method: POST

Description: Creates a new hotel entry.

Request Body: A JSON object with the hotel data.

Sample Request Body:
`{
  "name": "Hotel Ocean Breeze",
  "price": 250,
  "available": true
}`
Response: A JSON object confirming the hotel creation.
Sample Response:
`{
  "Message": "Added Successfully"
}`
