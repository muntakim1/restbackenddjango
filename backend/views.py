from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import productModel
from .serializers import productSerializer


class productViewset(viewsets.ModelViewSet):
    queryset = productModel.objects.all()
    serializer_class = productSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


def index(request):
    return render(request, 'index.html')
