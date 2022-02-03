from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ContactSerializer
from .models import ContactInfo

@api_view(['GET'])
def contact_list(request):
    q = ContactInfo.objects.all()
    serializer = ContactSerializer(q , many = True)
    return Response(serializer.data , status=status.HTTP_200_OK)

@api_view(['GET'])
def contact_detail(request):
    res = {}
    obj_id = request.GET.get('id')
    if ContactInfo.objects.filter(id = obj_id).exists():
        contact = ContactInfo.objects.get(id = obj_id)
        serializer = ContactSerializer(contact , many = False)
        res = serializer.data
    res['msg'] = "Contact details does not exist"
    return Response( res , status =  status.HTTP_200_OK)


@api_view(['POST'])
def contact_create(request):
    res = {}
    serializer = ContactSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    res['msg'] = "Contact info created successfully"
    res['data'] = serializer.data
    return Response(res, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def contact_update(request):
    res={}
    body = request.data
    curr_id = body['id']
    q = ContactInfo.objects.get(id = curr_id)
    serializer = ContactSerializer(instance = q ,data = body)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    res['msg'] = "Contact info updated successfully"
    res['data'] = serializer.data
    return Response(res, status=status.HTTP_200_OK)
