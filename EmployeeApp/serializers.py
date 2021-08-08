from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

"""
Serializers helps to convert complex type or models instances into native python data types 
that can be easily rendered into JSON or XML objects
"""
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')