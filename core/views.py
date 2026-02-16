from rest_framework import generics
from .models import Organize, Practice, Patient
from .serializers import OrganizeSerializer,PracticeSerializer,PatientSerializer

class OrganizeView(generics.ListCreateAPIView):
    queryset = Organize.objects.all()
    serializer_class = OrganizeSerializer


class PracticeView(generics.ListCreateAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer


class PatientView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer