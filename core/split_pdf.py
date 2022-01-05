from tabula import read_pdf
import re
from os import makedirs, getcwd
from os.path import exists, dirname, join
from PyPDF2.pdf import PdfFileReader, PdfFileWriter


def criar_pasta(pst):
    if not exists(pst):
        try:
            makedirs(pst)
        except Exception as e:
            print(f"ERRO EM CRIAR PASTA {e}")


def split_pdf(arquivo_entrada):
    pst_destino = join("media", "PDF", "saidaponto")
    criar_pasta(join(getcwd(), pst_destino))
    ponto = PdfFileReader(open(arquivo_entrada, 'rb'))
    funcionarios = read_pdf(arquivo_entrada, pages='all')

    for p in range(ponto.numPages):
        saida = PdfFileWriter()
        saida.addPage(ponto.getPage(p))
        funcionario = funcionarios[p].columns[0:1]
        with open(join(pst_destino, f"{funcionario[0]}.pdf".replace(':', '')), "wb") as saidaStream:
            saida.write(saidaStream)


def carregaholerite(pdf_arquivo):
    holerites = PdfFileReader(open(pdf_arquivo,  'rb'))
    pst_destino = join("media", "PDF", "holerite")
    criar_pasta(join(getcwd(), pst_destino))

    def f(x): return re.sub(r'\/|\\', '', x)

    for h in range(holerites.numPages):
        saida = PdfFileWriter()
        saida.addPage(holerites.getPage(h))
        pagina = holerites.getPage(h)
        conteudo = pagina.extractText()
        if len(re.findall(r'(\d.{3,4})+[0-9]{2,3} - (\w.+)', conteudo)) == 1:
            continue
        find = re.findall(r'(\d.{3,4})+[0-9]{2,3} - (\w.+)', conteudo)[0][-1]

        with open(join(pst_destino, f"{f(find)}.pdf"), "wb") as saidaStream:
            saida.write(saidaStream)
