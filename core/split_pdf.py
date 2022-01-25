from os import makedirs, getcwd
from re import findall, split, sub
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
    return str(image_to_string(img))


def transforma_pdf_img_funcionarios(pdf_arquivo, dst):
    print(f"INICIANDO O PROCESSAMENTO DO PDF {basename(pdf_arquivo)}")
    pst_destino = join(getcwd(), "media", "PDF", dst)
    criar_pasta(pst_destino)

    funcionarios = []
    pdftoimage = convert_from_path(pdf_arquivo)
    def d(x): return str(x).replace("\\", '').replace("\n", '')

    def l(x): return x if len(
        x) == 0 or '-' not in x else d(split("\s-\s|\n", str(x))[-1][:-3])

    total_paginas = len(pdftoimage)
    def i(x): return sub("[C|c]olaborador\:", '', x).strip()
    for inx in range(total_paginas):
        conteudo = extrair_texto(pdftoimage[inx])
        print(f"TENTANDO PAGINA {inx}/{total_paginas}")

        if conteudo == '' or len(str(conteudo)) in [0, 1]:
            continue

        l1 = findall("\n\d+\s-\s[\w|\s]+\s", conteudo)[-1]
        l2 = findall("colaborador\:?[\w |\s]*", conteudo, 2)
        try:
            funcionario = l(l1 if len(str(l1)) not in [0, 1, 2] else i(l2[0]))
            if funcionario == '' or len(str(funcionario)) in [0, 1, 2]:
                continue

            funcionario = ' '.join(funcionario.split(" ")[:3])
            funcionario += f"_{inx}.jpg"
            caminho_arquivo = join(pst_destino, funcionario)
            funcionarios.append({'nome': funcionario,
                                'caminho_arquivo': join("PDF", dst, funcionario)})
            print(caminho_arquivo)
            pdftoimage[inx].save(
                caminho_arquivo, 'JPEG'
            )
        except Exception as e:
            print(f"ERRO ENCONTRADO EM SPLITAR {e}")

    return funcionarios
