from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = Company
        fields = '__all__'
