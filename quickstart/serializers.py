from django.contrib.auth.models import Funcionario
from rest_framework import serializers


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'email']