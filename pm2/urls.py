from django.urls import path
from . import views

urlpatterns = [
    path('employee-details/', views.employee_details, name='employee_details'),
]
