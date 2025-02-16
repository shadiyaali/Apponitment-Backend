# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),

    path('attendance/', AttendanceListCreate.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceDetail.as_view(), name='attendance-detail'),
    
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    path('appointments/', AppointmentListCreate.as_view(), name='appointment-list-create'),  
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),   

    path('employee-count-today/', EmployeeCountTodayView.as_view(), name='employee-count-today'),
    path('appointments-today/', AppointmentTodayView.as_view(), name='appointments-today'),
    path('appointments-status-count/', AppointmentOddStatusCountView.as_view(), name='appointments-odd-status-count'),
]

