from .models import AutoPolicy
from rest_framework import serializers, viewsets

class AutoPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = AutoPolicy
        fields = '__all__'

class AutoPolicyViewSet(viewsets.ModelViewSet):
    queryset = AutoPolicy.objects.all()
    serializer_class = AutoPolicySerializer
