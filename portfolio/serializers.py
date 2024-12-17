from rest_framework import serializers

from .models import Projects

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__' 