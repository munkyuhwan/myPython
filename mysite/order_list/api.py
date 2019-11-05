from .models import OrderList
from rest_framework import serializers, viewsets

class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderList
        fields = '__all__'

class OrderListViewSet(viewsets.ModelViewSet):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer
