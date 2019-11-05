from .models import ActivityCheck
from rest_framework import serializers, viewsets

class ActivityCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityCheck
        fields = '__all__'

class ActivityCheckViewSet(viewsets.ModelViewSet):
    queryset = ActivityCheck.objects.all()
    serializer_class = ActivityCheckSerializer
