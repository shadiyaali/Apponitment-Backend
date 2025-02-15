# Appointment Backend

## Setup

# Clone the repository
```sh
git clone https://github.com/shadiyaali/Apponitment-Backend

# Setup Virtual Environment and Install Dependencies
```sh
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Run Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate


## API Endpoints

# Doctor Endpoints

# List all doctors
```sh
GET /booking/doctors/

# Create a new doctor
```sh
POST /booking/doctors/
Content-Type: application/json
Example JSON:
{
    "name": "Dr. John Doe",
    "specialization": "Cardiologist",
    "phone": "1234567890",
    "email": "johndoe@example.com"
}

# Retrieve a doctor
```sh
GET /booking/doctors/<id>/

# Update a doctor
```sh
PUT /booking/doctors/<id>/
Example JSON:
{
    "specialization": "Neurologist"
}

# Delete a doctor
```sh
DELETE /booking/doctors/<id>/


# Patient Endpoints

# List all patients
```sh
GET /booking/patients/

# Create a new patient
```sh
POST /booking/patients/
Example JSON:
{
    "name": "Jane Doe",
    "age": 30,
    "gender": "Female",
    "phone": "9876543210",
    "email": "janedoe@example.com"
}

# Retrieve a patient
```sh
GET /booking/patients/<id>/

# Update a patient
```sh
PUT /booking/patients/<id>/
Example JSON:
{
    "age": 35
}

# Delete a patient
```sh
DELETE /booking/patients/<id>/


# Appointment Endpoints

# List all appointments
```sh
GET /booking/appointments/

# Create a new appointment
```sh
POST /booking/appointments/
Example JSON:
{
    "patient": 1,
    "doctor": 2,
    "date": "2024-07-15",
    "time": "10:00:00",
    "status": "Booked"
}

# Retrieve an appointment
```sh
GET /booking/appointments/<id>/

# Update an appointment
```sh
PUT /booking/appointments/<id>/
Example JSON:
{
    "status": "Completed"
}

# Delete an appointment
```sh
DELETE /booking/appointments/<id>/
