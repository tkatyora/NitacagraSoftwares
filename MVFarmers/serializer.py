from rest_framework import serializers
from .models import Problems


class ProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problems
        fields = '__all__'
      