from django import forms
from firstapp import models

class studentform(forms.ModelForm):
    
    class Meta:
        model =models.Student 
        fields = "__all__"

class employeeform(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = "__all__"
