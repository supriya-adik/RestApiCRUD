from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin) :
    list_display = ['eno','ename','eaddr','esal']

admin.site.register(Employee,EmployeeAdmin)
