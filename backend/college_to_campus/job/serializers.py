from rest_framework import serializers
from .models import *


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'