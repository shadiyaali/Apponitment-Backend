# Appointment Backend

## Setup

### 1. Clone Repository
```sh
git clone https://github.com/shadiyaali/Apponitment-Backend


2. Setup Virtual Environment and Install Dependencies

sh
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Run Database Migrations
sh
    python manage.py makemigrations
    python manage.py migrate

 

API Usage Endpoints

Doctor Endpoints

List all doctors

GET /booking/doctors/

Create a new doctor

POST /booking/doctors/

Content-Type: application/json
Example JSON:

{
    "name": "Dr. John Doe",
    "specialization": "Cardiologist",
    "phone": "1234567890",
    "email": "johndoe@example.com"
}

Retrieve a doctor

GET /booking/doctors/<id>/

Update a doctor

PUT /booking/doctors/<id>/

Example JSON:

{
    "specialization": "Neurologist"
}

Delete a doctor

DELETE /booking/doctors/<id>/

Patient Endpoints

List all patients

GET /booking/patients/

Create a new patient

POST /booking/patients/

Example JSON:

{
    "name": "Jane Doe",
    "age": 30,
    "gender": "Female",
    "phone": "9876543210",
    "email": "janedoe@example.com"
}

Retrieve a patient

GET /booking/patients/<id>/

Update a patient

PUT /booking/patients/<id>/

Example JSON:

{
    "age": 35
}

Delete a patient

DELETE /booking/patients/<id>/

Appointment Endpoints

List all appointments

GET /booking/appointments/

Create a new appointment

POST /booking/appointments/

Example JSON:

{
    "patient": 1,
    "doctor": 2,
    "date": "2024-07-15",
    "time": "10:00:00",
    "status": "Booked"
}

Retrieve an appointment

GET /booking/appointments/<id>/

Update an appointment

PUT /booking/appointments/<id>/

Example JSON:

{
    "status": "Completed"
}

Delete an appointment 

DELETE /booking/appointments/<id>/