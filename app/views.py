from django.shortcuts import render

# Create your views here.

from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view()
def EmployeeData(request):
    EQS=Employee.objects.all()
    ESD=EmployeeMS(EQS,many=True)
    return Response(ESD.data)