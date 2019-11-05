from balance_check.models import BalanceCheck
#from balance_check.serializers import BalanceCheckSerializer
from balance_check.api import BalanceCheckSerializer
from rest_framework import generics

class BalanceCheck(generics.ListAPIView):
    serializer_class = BalanceCheckSerializer

    def get_queryset(self):
        queryset = BalanceCheck.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset
