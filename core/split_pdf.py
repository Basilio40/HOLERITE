from re import findall, split
from os import makedirs, getcwd
from pdf2image import convert_from_path
from pytesseract import image_to_string
from os.path import exists, dirname, join, basename


def criar_pasta(pst):
    if not exists(pst):
        try:
            makedirs(pst)
        except Exception as e:
            print(f"ERRO EM CRIAR PASTA {e}")


def extrair_texto(img):
    return image_to_string(img)


def transforma_pdf_img_funcionarios(pdf_arquivo, dst):
    print(f"INICIANDO O PROCESSAMENTO DO PDF {basename(pdf_arquivo)}")
    pst_destino = join(getcwd(), "media", "PDF", dst)
    criar_pasta(pst_destino)

    funcionarios = []
    pdftoimage = convert_from_path(pdf_arquivo)
    def l(x): return x if len(x) == 0 and '-' not in x else split("\s-\s|\n", str(x))[-1][:-3]
    for inx in range(len(pdftoimage)):
        conteudo = extrair_texto(pdftoimage[inx])

        if conteudo == '' or len(str(conteudo)) in [0, 1]:
            continue

        funcionario = l(findall("\n\d+\s-\s[\w|\\n]*", conteudo))
        if funcionario == '' or len(str(funcionario)) in [0, 1]:
            continue

        funcionario += f"_{inx}.jpg"
        funcionarios.append(funcionario)

        pdftoimage[inx].save(
            join(pst_destino, funcionario), 'JPEG'
        )

    return funcionarios
