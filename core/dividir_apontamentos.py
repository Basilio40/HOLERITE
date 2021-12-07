import tabula
import re
import os
from PyPDF2.pdf import PdfFileReader, PdfFileWriter

#=======================================LENDO DADOS DOS HOLERITES DOS FUNCIONARIOS===================================================     
class CarregarPdf:
    def __init__(self):
        pass
def split_pdf(arquivo_entrada):
        ponto = PdfFileReader(open(arquivo_entrada , 'rb'))
        funcionarios = tabula.read_pdf(arquivo_entrada, pages='all')
        for p in range(ponto.numPages):
            saida = PdfFileWriter()
            saida.addPage(ponto.getPage(p))
            funcionario = funcionarios[p].columns[0:1]
            with open(f"media/{funcionario[0]}.pdf".replace(':',''), "wb") as saidaStream:
                saida.write(saidaStream)

