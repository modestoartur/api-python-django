from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.serializers import *
from .models import Funcionario
from quickstart.serializers import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite o funcionar ser visto e alterado.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAuthenticated]