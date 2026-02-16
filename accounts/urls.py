from django.urls import path
from .views import ClaimList, PaymentView

urlpatterns = [
    path('claims/', ClaimList.as_view()),
    path('payments/', PaymentView.as_view()),
]
