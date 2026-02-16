from django.urls import path
from .views import OrganizeView, PracticeView, PatientView

urlpatterns = [
    path('organize/', OrganizeView.as_view()),
    path('practices/', PracticeView.as_view()),
    path('patients/', PatientView.as_view()),
]