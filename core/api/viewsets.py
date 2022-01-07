from core.api import serializers
from rest_framework import viewsets
from core import models


class FilePdfViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.FilePdfSerializer
    queryset = models.FilePdf.objects.all()


class FuncionarioViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.FuncionarioSerializer
    queryset = models.Funcionario.objects.all()


class PontoViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.PontoSerializer
    queryset = models.Ponto.objects.all()


class HoleriteViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.HoleriteSerializer
    queryset = models.Holerite.objects.all()
