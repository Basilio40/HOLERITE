from os.path import exists, dirname, join, basename
from os import makedirs, getcwd, rename
from re import findall, split, sub, IGNORECASE
from pytesseract import image_to_string
from datetime import datetime
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


def renomear_png(entrada, saida):
    try:
        rename(entrada, saida)
        print(f"RENOMEANDO {basename(entrada)} {saida}")
        return True
    except Exception as e:
        print(f"ERRO EM RENOMEAR {e}")
        return False


def transforma_pdf_img_funcionarios(instancia, dst):
    print(f"INICIANDO O PROCESSAMENTO DO PDF {basename(instancia.caminho_arquivo.path)}")
    pst_destino = join(getcwd(), "media", "PDF", dst)
    criar_pasta(pst_destino)

    funcionarios = []
    CAMINHO_TMP = join(
        pst_destino, f"PDF_{instancia.ano}_{instancia.mes}_{datetime.now().strftime('%d%m%Y%H%M')}")
    criar_pasta(CAMINHO_TMP)
    run_split(instancia.caminho_arquivo.path, join(CAMINHO_TMP, 'pdf_'))

    def d(x): return str(x).replace("\\", '').replace("\n", '')

    def l(x): return x if len(
        x) == 0 or '-' not in x else d(split("\s-\s|\n", str(x))[-1])

    pngs = glob(join(CAMINHO_TMP, "*.png"))
    def i(x): return sub("[C|c]olaborador\:", '', x).strip()

    for e, png in enumerate(pngs):
        conteudo = extrair_texto(png)
        print(f"TENTANDO PAGINA {e}/{len(pngs)}")

        if conteudo == '' or len(str(conteudo)) in [0, 1]:
            continue

        try:
            l1 = findall("\n\d+\s-\s[\w|\s]+\s", conteudo)[-1]
        except:
            l1 = ''

        try:
            l2 = findall("colaborador\:?[\w |\s]*", conteudo, IGNORECASE)
            funcionario = l(l1 if len(str(l1)) not in [0, 1, 2] else i(l2[0]))
            if funcionario == '' or len(str(funcionario)) in [0, 1, 2]:
                continue

            funcionario = ' '.join(funcionario.split(" ")[:3])
            caminho_arquivo = join(pst_destino, funcionario)
            caminho_novo = join(dirname(png), f"{basename(funcionario)}.png")

            ren = renomear_png(png, caminho_novo)
            if ren:
                caminho_arquivo = caminho_novo

            funcionarios.append({'nome': funcionario,
                                'caminho_arquivo': '/PDF' + caminho_novo.split(r'/media/PDF')[1]})

        except Exception as e:
            print(f"ERRO ENCONTRADO EM SPLITAR {e}")

    return funcionarios
