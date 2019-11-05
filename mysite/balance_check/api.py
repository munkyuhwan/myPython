from .models import BalanceCheck
from rest_framework import serializers, viewsets


class BalanceCheckSerializer(serializers.ModelSerializer):

    class Meta:
        model = BalanceCheck
        fields = '__all__'

class BalanceCheckViewSet(viewsets.ModelViewSet):
    queryset = BalanceCheck.objects.all()
    serializer_class = BalanceCheckSerializer
