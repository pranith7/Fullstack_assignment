from rest_framework import generics
from .models import Interest
from .serializers import InterestSerializer
from rest_framework.permissions import IsAuthenticated

class InterestListCreate(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]
class InterestUpdate(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [IsAuthenticated]
