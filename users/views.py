from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET',])
def smoke(request):
    return Response('i\'m a teapot', status=status.HTTP_418_IM_A_TEAPOT)
