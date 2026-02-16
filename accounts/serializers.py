from rest_framework import serializers
from .models import Claim, Payment

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '_all_'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '_all_'