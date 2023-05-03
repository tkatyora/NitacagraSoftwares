from django.shortcuts import render
from Ourservices.models import *
from django.http import JsonResponse
from .serializer import ServiceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
serviceinfo = servicesTable.objects.all()
# view for sendig api for viewing data
@api_view(['GET',])
def viewServiceApi(request):
    if request.method == 'GET':
        services = ServiceSerializer(serviceinfo, many=True)
        return Response(services.data)
#API FUNCTION
@api_view(['POST',])
def createServiceApi(request):
    if request.method == 'POST':
        #the service we are going to create
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = servicesTable(
                section=serializer.data['section'],
                name=serializer.data['name'],
                briefDisc=serializer.data['briefDisc'],
                FullDisc=serializer.data['FullDisc'],
                oldPrice=serializer.data['oldPrice'],
                newPrice=serializer.data['newPrice'],
                specialOffer=serializer.data['specialOffer'],
                
            )
            service.save()
            _serializer = ServiceSerializer(service)
            return Response(service)
        