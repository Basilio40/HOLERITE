from os import makedirs, getcwd
from re import findall, split, sub
from pytesseract import image_to_string
from os.path import exists, dirname, join, basename
from tempfile import gettempdir
from random import randint
from subprocess import run
from glob import glob


def criar_pasta(pst):
    if not exists(pst):
        try:
            makedirs(pst)
        except Exception as e:
            print(f"ERRO EM CRIAR PASTA {e}")


def extrair_texto(img):
    return str(image_to_string(img))


def run_split(entrada, saida):
    run(["pdftoppm", "-png", entrada, saida])


def transforma_pdf_img_funcionarios(pdf_arquivo, dst):
    print(f"INICIANDO O PROCESSAMENTO DO PDF {basename(pdf_arquivo)}")
    pst_destino = join(getcwd(), "media", "PDF", dst)
    criar_pasta(pst_destino)

    funcionarios = []
    CAMINHO_TMP = join(gettempdir(), f"PDF_{randint(10000, 100000)}")
    criar_pasta(CAMINHO_TMP)
    run_split(pdf_arquivo, join(CAMINHO_TMP, 'pdf_'))

    def d(x): return str(x).replace("\\", '').replace("\n", '')

    def l(x): return x if len(
        x) == 0 or '-' not in x else d(split("\s-\s|\n", str(x))[-1][:-3])

    pngs = glob(join(CAMINHO_TMP, "*.png"))
    def i(x): return sub("[C|c]olaborador\:", '', x).strip()

    for e, png in enumerate(pngs):
        conteudo = extrair_texto(png)
        print(f"TENTANDO PAGINA {e}/{len(pngs)}")

        if conteudo == '' or len(str(conteudo)) in [0, 1]:
            continue

        l1 = findall("\n\d+\s-\s[\w|\s]+\s", conteudo)[-1]
        l2 = findall("colaborador\:?[\w |\s]*", conteudo, 2)
        try:
            funcionario = l(l1 if len(str(l1)) not in [0, 1, 2] else i(l2[0]))
            if funcionario == '' or len(str(funcionario)) in [0, 1, 2]:
                continue

            funcionario = ' '.join(funcionario.split(" ")[:3])
            funcionario += f"_{png}.jpg"
            caminho_arquivo = join(pst_destino, funcionario)
            funcionarios.append({'nome': funcionario,
                                'caminho_arquivo': join("PDF", dst, funcionario)})
            print(caminho_arquivo)

        except Exception as e:
            print(f"ERRO ENCONTRADO EM SPLITAR {e}")

    return funcionarios
