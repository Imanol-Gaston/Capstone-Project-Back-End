# Freelance Industrial Inspectors Application Documentation

## Description
This Flask application provides a service for finding freelance industrial inspectors. It exposes three endpoints to interact with inspector profiles.

## Endpoints

### 1. Get All Inspector Profiles

#### Description
This endpoint returns all profiles of industrial inspectors stored in the database.

#### https://capstone-project-back-end-production.up.railway.app/api/v1/profiles

#### GET PROFILES

#### Request Parameters
None.

#### Successful Response
Status Code: 200 OK
```json
[
  {
    "id": 1,
    "user_id": 1001,
    "brief_description": "Brief description of the inspector",
    "created_at": "Timestamp of creation",
    "fullname": "Inspector Full Name",
    "full_description": "Full description of the inspector",
    "experiences": [
      {
        "id": 101,
        "user_id": 1001,
        "role": "Inspector Role",
        "supplier": "Supplier Name",
        "product": "Product Inspected",
        "location": "Inspection Location",
        "category": "Inspection Category",
        "description": "Inspection Description",
        "year": 2022
      },
      // Other experiences...
    ]
  },
  // Other profiles...
]

2. Get Individual Inspector Profile
Description
This endpoint returns details of a specific inspector's profile.

URL

GET /profiles/{id}

Request Parameters
{id}: Unique identifier of the inspector.
Successful Response
Status Code: 200 OK

{
  "id": 1,
  "user_id": 1001,
  "brief_description": "Brief description of the inspector",
  "created_at": "Timestamp of creation",
  "fullname": "Inspector Full Name",
  "full_description": "Full description of the inspector",
  "experiences": [
    {
      "id": 101,
      "user_id": 1001,
      "role": "Inspector Role",
      "supplier": "Supplier Name",
      "product": "Product Inspected",
      "location": "Inspection Location",
      "category": "Inspection Category",
      "description": "Inspection Description",
      "year": 2022
    },
    // Other experiences...
  ]
}

3. Add Inspector Profile
Description
This endpoint allows adding a new inspector profile.

URL

POST /profiles

Request Body

{
  "user_id": 1001,
  "brief_description": "Brief description of the inspector",
  "fullname": "Inspector Full Name",
  "full_description": "Full description of the inspector"
}

Successful Response
Status Code: 201 Created

{
  "id": 102,
  "user_id": 1001,
  "brief_description": "Brief description of the inspector",
  "created_at": "Timestamp of creation",
  "fullname": "Inspector Full Name",
  "full_description": "Full description of the inspector"
}

Usage Examples
Get All Inspector Profiles

curl -X GET https://web-production-edbf.up.railway.app/profiles

Get Individual Inspector Profile

curl -X GET https://web-production-edbf.up.railway.app/profiles/1

Add Inspector Profile

curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1001, "brief_description": "Brief description of the inspector", "fullname": "Inspector Full Name", "full_description": "Full description of the inspector"}' https://web-production-edbf.up.railway.app/profiles



