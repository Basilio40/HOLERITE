from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from core.dividir_apontamentos import split_pdf
from core.dividir_holerites import carregaholerite


class MixData(models.Model):
    data_insercao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Registro"
    )
    data_modificacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Modificação"
    )
    class Meta:
        abstract = True

class FilePdf(MixData):
    caminho_arquivo = models.FileField()
    nome_arquivo = models.CharField(max_length=100)


class Holerite(FilePdf):
    mes = models.DateField()
    ano = models.IntegerField()    


class Ponto(FilePdf):
    mes_choices = (("Jan", "Janeiro"), ("Fev", "Feveiro"), ("Mar", "Março"),("Abr" , "Abril"),("Mai","Maio"),("Jun","Junho"),("Jul","Julho"),("Ago","Agosto"),("Set","Setembro"),
                   ("Out","Outubro"),("Nov","Novembro"),("Dez","Dezembro"),)
    mes = models.CharField(max_length=4, choices=mes_choices,
                        default=mes_choices[0][0],)
    ano = models.IntegerField()
    
    def __str__(self) :
        return self.mes


class Funcionario(MixData):
    nome = models.CharField(max_length=100)
    holerite = models.ForeignKey(Holerite, on_delete=models.CASCADE)
    ponto = models.ForeignKey(Ponto, on_delete=models.CASCADE)


@receiver(post_save, sender=Holerite)
def pos_save_ponto(instance, created, **kargs):
    print(f"SALVANDO O {instance.caminho_arquivo}")
    split_pdf(instance.caminho_arquivo.path)

@receiver(post_save, sender=Ponto)
def pos_save_holerite(instance, created, **kargs):
    print(f"SALVANDO O {instance.caminho_arquivo}")
    carregaholerite(instance.caminho_arquivo.path)