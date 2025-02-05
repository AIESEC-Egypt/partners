from rest_framework import generics
from .models import PartnerApplication
from .serializers import PartnerApplicationSerializer

class PartnerApplicationCreateView(generics.CreateAPIView):
    queryset = PartnerApplication.objects.all()
    serializer_class = PartnerApplicationSerializer
