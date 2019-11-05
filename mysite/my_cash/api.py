from .models import MyCash
from rest_framework import serializers, viewsets

class MyCashSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyCash
        fields = '__all__'

class MyCashViewSet(viewsets.ModelViewSet):
    queryset = MyCash.objects.all()
    serializer_class = MyCashSerializer
