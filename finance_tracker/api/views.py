from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrAdmin
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

# Create your views here.
def homeAPI(request):
    return HttpResponse("Home of the API")


#class TransactionList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#class TransactionDetail(APIView):

    #permission_classes = [IsOwnerOrAdmin]
    def get(self, request, pk):
        try:
            transaction = Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction was not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TransactionSerializer(transaction, context={'request': request})
        return Response(serializer.data)


class TransactionList(ListCreateAPIView):
    """
    Handles listing all transactions and creating new ones.
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TransactionDetail(RetrieveDestroyAPIView):
    """
    Handles retrieving or deleting a specific transaction
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer