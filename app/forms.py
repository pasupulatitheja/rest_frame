from django import forms
from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        esal_input = self.cleaned_data['esalary']
        if esal_input < 5000:
            raise forms.ValidationError("minimum salary should be 5000")
        return esal_input

    class Meta:
        model = EmployeeModel
        fields = '__all__'

