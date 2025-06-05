from django.urls import path
from .views import homeAPI, TransactionList, TransactionDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', homeAPI),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
    path("transactions/<int:pk>", TransactionDetail.as_view(), name="transaction-detail"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
