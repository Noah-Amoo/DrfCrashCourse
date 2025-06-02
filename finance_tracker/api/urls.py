from django.urls import path
from .views import homeAPI

urlpatterns = [
    path('', homeAPI)
]
