import django_filters
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from api.pagination import LargeResultsSetPagination
from api.permissions import IsAdminUserOrReadOnly
from api.serializers import OrgShippingPreferenceSerializer
from api.models.ec.orgshippingpreference import OrgShippingPreference


class OrgShippingPreferenceFilter(django_filters.FilterSet):
    class Meta:
        model = OrgShippingPreference
        fields = ['organization','is_pickup_only',]


class OrgShippingPreferenceViewSet(viewsets.ModelViewSet):
    queryset = OrgShippingPreference.objects.all()
    serializer_class = OrgShippingPreferenceSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_class = OrgShippingPreferenceFilter