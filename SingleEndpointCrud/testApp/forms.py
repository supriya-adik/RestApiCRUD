from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm) :
    class Meta :
        model=Employee
        fields='__all__'

    def clean_esal(self):
        inputsal=self.cleaned_data['esal']
        if inputsal <5000 :
            raise forms.ValidationError('The Minimum Salary should be 50000')
        return inputsal