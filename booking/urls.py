from django.urls import path
from .views import *

urlpatterns = [
    # Doctor Routes
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Patient Routes
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Appointment Routes
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]
