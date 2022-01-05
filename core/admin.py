from django.contrib import admin
from .models import FilePdf, Ponto, Holerite, Funcionario


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "holerite", "ponto"]
    list_filter = ["nome"]

    class Meta:
        model = Funcionario


class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "caminho_arquivo"]

    class Meta:
        model = FilePdf


class HoleriteAdmin(admin.ModelAdmin):
    list_display = ('mes', 'ano', "caminho_arquivo")

    class Meta:
        model = Holerite


class PontoAdmin(HoleriteAdmin):
    class Meta:
        model = Ponto


admin.site.register(FilePdf, FileAdmin)
admin.site.register(Ponto, PontoAdmin)
admin.site.register(Holerite, HoleriteAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
