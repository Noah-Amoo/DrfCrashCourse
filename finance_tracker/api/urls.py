from django.urls import path
from .views import homeAPI, TransactionList

urlpatterns = [
    path('', homeAPI),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
    path("transactions/<int:pk>", TransactionDetail.as_view(), name="transaction-detail"),
]
