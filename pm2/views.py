from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Employee

def employee_details(request):
    employees = Employee.objects.all()
    selected_employee = None
    search_query = request.GET.get('search_query', '')

    if search_query:
       
        selected_employee = Employee.objects.filter(
            employee_id=search_query
        ).first() or Employee.objects.filter(
            first_name__icontains=search_query
        ).first() or Employee.objects.filter(
            last_name__icontains=search_query
        ).first()
    
    if selected_employee:
        
        today = now().date()
        age = today.year - selected_employee.date_of_birth.year - (
            (today.month, today.day) < (selected_employee.date_of_birth.month, selected_employee.date_of_birth.day)
        )
    else:
        age = None

    return render(request, 'pm2/employee_details.html', {
        'employees': employees,
        'selected_employee': selected_employee,
        'age': age,
    })
