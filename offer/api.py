from rest_framework import viewsets
from .serializers import OfferSerializer

from .models import offer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = offer.objects.all()
    serializer_class = OfferSerializer
