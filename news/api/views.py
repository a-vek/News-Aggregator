from news.models import Headline
from .serializers import HeadlineSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class HeadlineViewSet(viewsets.ModelViewSet):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    filterset_fields = ['category']
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
