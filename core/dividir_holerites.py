import re
from PyPDF2.pdf import PdfFileReader, PdfFileWriter


def carregaholerite(holerites):
    holerites = PdfFileReader(open(r"C:\Users\Sandro Bispo\Desktop\Pythons_do_mes\projeto_vetor\Holerite\HOLERITES 10-2020.pdf",'rb'))
    f = lambda x: re.sub(r'\/|\\', '', x)
    for h in range(holerites.numPages):
        saida = PdfFileWriter()
        saida.addPage(holerites.getPage(h))
        pagina = holerites.getPage(h)
        conteudo = pagina.extractText()
        if len(re.findall(r'(\d.{3,4})+[0-9]{2,3} - (\w.+)', conteudo)) == 1:
            continue
        find = re.findall(r'(\d.{3,4})+[0-9]{2,3} - (\w.+)', conteudo)[0][-1]
        with open(f"media/saidaholerite/{f(find)}.pdf", "wb") as saidaStream:
            saida.write(saidaStream)