from rest_framework import serializers
from core import models


class FilePdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilePdf
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Funcionario
        fields = '__all__'


class PontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ponto
        fields = '__all__'


class HoleriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holerite
        fields = '__all__'
