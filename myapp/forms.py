from .models import Student
from django import forms


class student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'f_name', 'sclass']
        labels = {'f_name': 'Father Name', 'sclass':'Class'}
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'f_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sclass': forms.TextInput(attrs={'class': 'form-control'})
        }
