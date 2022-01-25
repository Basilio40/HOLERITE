from os import makedirs
from django.db import models
from django.dispatch import receiver
from os.path import join, exists, dirname
from django.db.models.signals import post_save
from core.split_pdf import transforma_pdf_img_funcionarios
from django.conf import settings


def caminho_upload(src, instance):
    def verificar_caminho_cria(caminho):
        caminho_arquivo = dirname(join(settings.MEDIA_ROOT, settings.PDFS))
        if not exists(caminho_arquivo):
            try:
                makedirs(caminho_arquivo)
                return True
            except Exception as e:
                print(f"ERRO ENCONTRADO AO TENTAR CRIAR CAMINHO {caminho} {e}")
                return False

    caminho_arquivo = join(settings.PDFS, instance)
    if not verificar_caminho_cria(caminho_arquivo):
        return caminho_arquivo
    return False


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
    caminho_arquivo = models.FileField(upload_to=caminho_upload)

    def __str__(self):
        return f"{self.caminho_arquivo}"


class Holerite(FilePdf):
    mes_choices = (("Jan", "Janeiro"), ("Fev", "Feveiro"), ("Mar", "Março"),
                   ("Abr", "Abril"), ("Mai", "Maio"), ("Jun", "Junho"), ("Jul", "Julho"),
                   ("Ago", "Agosto"), ("Set", "Setembro"), ("Out", "Outubro"),
                   ("Nov", "Novembro"), ("Dez", "Dezembro"),)
    mes = models.CharField(max_length=4, choices=mes_choices,
                           default=mes_choices[0][0],)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.mes} {self.ano} " + super().__str__()


class Ponto(FilePdf):
    mes_choices = (("Jan", "Janeiro"), ("Fev", "Feveiro"), ("Mar", "Março"),
                   ("Abr", "Abril"), ("Mai", "Maio"), ("Jun", "Junho"), ("Jul", "Julho"),
                   ("Ago", "Agosto"), ("Set", "Setembro"), ("Out", "Outubro"),
                   ("Nov", "Novembro"), ("Dez", "Dezembro"),)
    mes = models.CharField(max_length=4, choices=mes_choices,
                           default=mes_choices[0][0],)
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.mes} {self.ano} " + super().__str__()


class Funcionario(MixData):
    nome = models.CharField(max_length=100)
    holerite = models.ForeignKey(Holerite, on_delete=models.CASCADE, null=True)
    ponto = models.ForeignKey(Ponto, on_delete=models.CASCADE, null=True)
    caminho_arquivo = models.FileField(upload_to=caminho_upload)

    def __str__(self):
        return f"{self.nome} {self.holerite} {self.ponto}"


@receiver(post_save, sender=Ponto)
def pos_save_ponto(instance, created, **kargs):
    def registrar_funcionarios(funcionarios):
        try:
            [Funcionario.objects.create(nome=func['nome'], holerite=instance.holerite,
                                        caminho_arquivo=func['caminho_arquivo'])
             for func in funcionarios]
        except Exception as e:
            print(f"ERRO EM TENTAR REGISTRAR FUNCIONARIOS {e}")
    funcionarios = transforma_pdf_img_funcionarios(instance.caminho_arquivo.path, 'PONTO')
    registrar_funcionarios(funcionarios)


@receiver(post_save, sender=Holerite)
def pos_save_holerite(instance, created, **kargs):
    def registrar_funcionarios(funcionarios):
        try:
            [Funcionario.objects.create(nome=func['nome'], holerite=instance.holerite,
                                        caminho_arquivo=func['caminho_arquivo'])
             for func in funcionarios]
        except Exception as e:
            print(f"ERRO EM TENTAR REGISTRAR FUNCIONARIOS {e}")
    funcionarios = transforma_pdf_img_funcionarios(instance.caminho_arquivo.path, 'HOLERITE')
    registrar_funcionarios(funcionarios)
