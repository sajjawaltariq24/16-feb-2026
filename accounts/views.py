from rest_framework import generics
from .models import Claim, Payment
from .serializers import ClaimSerializer, PaymentSerializer

class ClaimList(generics.ListCreateAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class PaymentView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer