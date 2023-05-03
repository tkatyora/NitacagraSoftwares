from rest_framework import serializers
from Ourservices.models import servicesTable


class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = servicesTable
        fields = ['section','name','briefDisc','FullDisc','oldPrice','newPrice','specialOffer']