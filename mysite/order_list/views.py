from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from order_list.models import OrderList
from order_list.api import OrderListSerializer

@api_view(['GET', 'POST'])
def order_list(request, format=None):
	if request.method == 'GET':
		orderList = OrderList.objects.all()
		serializer = OrderListSerializer(orderList, many=True) # many 값이 True 이면 다수의 데이터 instance를 직렬화할수 있다
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = OrderListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


















