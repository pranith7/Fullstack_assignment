from rest_framework import generics
from .models import Interest
from .serializers import InterestSerializer

class InterestListCreate(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
class InterestUpdate(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer