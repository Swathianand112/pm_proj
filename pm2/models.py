from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    project_id = models.CharField(max_length=10, unique=True)
    project_name = models.CharField(max_length=100)
    project_manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name

class ProjectAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='projects')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    allocation_percentage = models.PositiveIntegerField()

    class Meta:
        unique_together = ('employee', 'project')


    def __str__(self):
        return f"{self.employee} assigned to {self.project} ({self.allocation_percentage}%)"