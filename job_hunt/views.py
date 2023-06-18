from django.shortcuts import render
from rest_framework import viewsets

from job_hunt.models import Company
from job_hunt.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
