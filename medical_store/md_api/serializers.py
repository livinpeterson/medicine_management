from medicine_management.models import Medicine
from rest_framework import serializers

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [ 'name',
            'available',
            'price',]