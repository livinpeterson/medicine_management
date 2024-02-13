from django import forms
from .models import Medicine

class Medicineform(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = [
            'name',
            'available',
            'price',
        ]
