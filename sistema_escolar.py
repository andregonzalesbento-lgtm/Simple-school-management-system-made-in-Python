import json

ARQUIVO = "alunos.json"
TOTAL_AULAS = 200   # exemplo anual

# CORES
verde = "\033[92m"
vermelho = "\033[91m"
amarelo = "\033[93m"
reset = "\033[0m"

# -------------------------
# ARQUIVO
# -------------------------

def carregar_alunos():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []

def salvar_alunos(alunos):
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)

alunos = carregar_alunos()

# -------------------------
# CALCULAR STATUS
# -------------------------

def calcular_status(media, faltas):

    limite_faltas = TOTAL_AULAS * 0.25

    if faltas > limite_faltas:
        return "Reprovado por falta"

    if media >= 6:
        return "Aprovado"

    return "Reprovado por nota"

# -------------------------
# CADASTRAR
# -------------------------

def cadastrar_aluno():

    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    faltas = int(input("Quantidade de faltas: "))

    media = (nota1 + nota2) / 2
    status = calcular_status(media, faltas)

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "faltas": faltas,
        "status": status
    }

    alunos.append(aluno)
    salvar_alunos(alunos)

    print(verde + "Aluno cadastrado!" + reset)

# -------------------------
# LISTAR
# -------------------------

def listar_alunos():

    if not alunos:
        print("Nenhum aluno cadastrado")
        return

    print("\n===== LISTA DE ALUNOS =====")

    for aluno in alunos:

        cor = verde if "Aprovado" in aluno["status"] else vermelho

        print(
            cor +
            f"{aluno['nome']} | Média: {aluno['media']:.2f} | Faltas: {aluno['faltas']} | {aluno['status']}"
            + reset
        )

# -------------------------
# PESQUISAR
# -------------------------

def pesquisar_aluno():

    nome = input("Nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            print("\n===== ALUNO =====")
            print("Nome:", aluno["nome"])
            print("Nota1:", aluno["nota1"])
            print("Nota2:", aluno["nota2"])
            print("Média:", f"{aluno['media']:.2f}")
            print("Faltas:", aluno["faltas"])
            print("Situação:", aluno["status"])
            return

    print("Aluno não encontrado")

# -------------------------
# EDITAR
# -------------------------

def editar_nota():

    nome = input("Aluno para editar: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            aluno["nota1"] = float(input("Nova nota1: "))
            aluno["nota2"] = float(input("Nova nota2: "))
            aluno["faltas"] = int(input("Novas faltas: "))

            aluno["media"] = (aluno["nota1"] + aluno["nota2"]) / 2
            aluno["status"] = calcular_status(aluno["media"], aluno["faltas"])

            salvar_alunos(alunos)

            print(amarelo + "Dados atualizados!" + reset)
            return

    print("Aluno não encontrado")

# -------------------------
# REMOVER
# -------------------------

def remover_aluno():

    nome = input("Aluno para remover: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            alunos.remove(aluno)
            salvar_alunos(alunos)

            print(vermelho + "Aluno removido!" + reset)
            return

    print("Aluno não encontrado")

# -------------------------
# RANKING
# -------------------------

def ranking():

    if not alunos:
        print("Nenhum aluno cadastrado")
        return

    ordenado = sorted(alunos, key=lambda x: x["media"], reverse=True)

    print("\n===== RANKING DA TURMA =====")

    for i, aluno in enumerate(ordenado, start=1):

        print(f"{i}º {aluno['nome']} - Média {aluno['media']:.2f}")

# -------------------------
# INFO MEC
# -------------------------

def info_faltas():

    print("\n===== REGRA DE FREQUÊNCIA =====")
    print("Presença mínima: 75%")
    print("Máximo de faltas: 25% das aulas")
    print("Base legal: Lei de Diretrizes e Bases da Educação (LDB)\n")

# -------------------------
# MENU
# -------------------------

while True:

    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Editar aluno")
    print("5 - Remover aluno")
    print("6 - Ranking da turma")
    print("7 - Regras de faltas")
    print("8 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar_aluno()

    elif op == "2":
        listar_alunos()

    elif op == "3":
        pesquisar_aluno()

    elif op == "4":
        editar_nota()

    elif op == "5":
        remover_aluno()

    elif op == "6":
        ranking()

    elif op == "7":
        info_faltas()

    elif op == "8":
        print("Sistema encerrado")
        break

    else:
        print("Opção inválida")

