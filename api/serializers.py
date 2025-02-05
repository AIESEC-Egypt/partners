from rest_framework import serializers
from .models import PartnerApplication

class PartnerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerApplication
        fields = '__all__'
