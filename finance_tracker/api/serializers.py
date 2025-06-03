from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.modelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'transaction_type', 'date', 'description']

    # DRF follows the validate_<fieldname> to check for which field to validate, in this case, amount.
    def validate_amount(self, value):
        if value <=0:
            raise serializers.ValidationError("Amount must be greater than zero")
        
        return value