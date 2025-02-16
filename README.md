# Appointment Backend

## Setup


# Deployed API

The backend is deployed on Render. You can access it at:
```sh
https://apponitment-backend.onrender.com

```
# Clone the repository
```sh
git clone https://github.com/shadiyaali/Apponitment-Backend
```
# Setup Virtual Environment and Install Dependencies

```sh
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
# Run Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```


## API Endpoints

# Doctor Endpoints

# List all doctors
```sh
GET /booking/doctors/
https://apponitment-backend.onrender.com/booking/doctors/
```
# Create a new doctor
```sh
POST /booking/doctors/
https://apponitment-backend.onrender.com/booking/doctors/
```
Content-Type: application/json
Example JSON
``` json:
{
    "name": "Dr. John Doe",
    "specialization": "Cardiologist",
    "phone": "1234567890",
    "email": "johndoe@example.com"
}
```
# Retrieve a doctor
```sh
GET /booking/doctors/<id>/
https://apponitment-backend.onrender.com/booking/doctors/<id>/
```
# Update a doctor
```sh
PUT /booking/doctors/<id>/
https://apponitment-backend.onrender.com/booking/doctors/<id>/
```
Example JSON
```json:
{
    "specialization": "Neurologist"
}
```
# Delete a doctor
```sh
DELETE /booking/doctors/<id>/
https://apponitment-backend.onrender.com/booking/doctors/<id>/
```

# Patient Endpoints

# List all patients
```sh
GET /booking/patients/
https://apponitment-backend.onrender.com/booking/patients/
```
# Create a new patient
```sh
POST /booking/patients/
https://apponitment-backend.onrender.com/booking/patients/
```
Example JSON
```json:
{
    "name": "Jane Doe",
    "age": 30,
    "gender": "Female",
    "phone": "9876543210",
    "email": "janedoe@example.com"
}
```
# Retrieve a patient
```sh
GET /booking/patients/<id>/
https://apponitment-backend.onrender.com/booking/patients/<id>/
```
# Update a patient
```sh
PUT /booking/patients/<id>/
https://apponitment-backend.onrender.com/booking/patients/<id>/
```
Example JSON
```json:
{
    "age": 35
}
```
# Delete a patient
```sh
DELETE /booking/patients/<id>/
https://apponitment-backend.onrender.com/booking/patients/<id>/
```

# Appointment Endpoints

# List all appointments
```sh
GET /booking/appointments/
https://apponitment-backend.onrender.com/booking/appointments/
```
# Create a new appointment
```sh
POST /booking/appointments/
https://apponitment-backend.onrender.com/booking/appointments/
```
Example JSON
```json:
{
    "patient": 1,
    "doctor": 2,
    "date": "2024-07-15",
    "time": "10:00:00",
    "status": "Booked"
}
```
# Retrieve an appointment
```sh
GET /booking/appointments/<id>/
https://apponitment-backend.onrender.com/booking/appointments/<id>/
```
# Update an appointment
```sh
PUT /booking/appointments/<id>/
https://apponitment-backend.onrender.com/booking/appointments/<id>/
```
Example JSON
``` json:
{
    "status": "Completed"
}
```
# Delete an appointment
```sh
DELETE /booking/appointments/<id>/
https://apponitment-backend.onrender.com/booking/appointments/<id>/
```
# Error Response Examples

Duplicate Doctor
```sh 
{
    "error": "Doctor with this email already exists."
}
```
Doctor Not Found
```sh
{
    "error": "Doctor not found!"
}
```
Patient Errors

Duplicate Patient
```sh
{
    "error": "Patient with this email  already exists."
}
```
Patient Not Found
```sh
{
    "error": "Patient not found!"
}
```
Appointment Errors
Doctor Already Booked
```sh 
{
    "error": "Doctor is already booked at this time!"
}
```
Patient Already Has an Appointment
```sh
{
    "error": "Patient already has an appointment at this time!"
}
```
Cannot Select Past Date and Time
```sh
{
    "error": "Cannot select past date and time for an appointment!"
}
```
Appointment Not Found
```sh
{
    "error": "Appointment not found!"
}
```
### Running Tests

To ensurebthe functionality of the API, you can run the tests

1. ** Run Unit Tests**:
     ```bash
     python manage.py test core 
     ```



