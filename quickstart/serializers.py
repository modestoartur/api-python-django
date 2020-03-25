from rest_framework import serializers
from .models import Funcionario


class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['url', 'nome', 'sobrenome', 'email']