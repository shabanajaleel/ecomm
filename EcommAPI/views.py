from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from EcomAdmin.models import Customer

# Create your views here.
@csrf_exempt
def fnapi_register(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data={'response_code':0,'message':"Successfully Registered"}
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)