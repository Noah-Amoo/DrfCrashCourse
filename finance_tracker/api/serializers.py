from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.modelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'date', 'description']