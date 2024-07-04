import os
import time

def limparTela():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac e Linux (posix)
    else:
        os.system('clear')

def aguardar(segundos):
    time.sleep(segundos)

while True:
    limparTela()
    print("(0) Sair")
    print("(1) Incluir Aluno")
    print("(2) Mostrar Lista")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome: ")
        email = input("E-mail: ")
        with open("bd.atitus", "a") as arquivo: # Usa modo append para adicionar ao arquivo sem sobrescrever
            arquivo.write(f"{nome} {email}\n")
        aguardar(2)
    elif opcao == "2":
        limparTela()
        print("Lista de Alunos:")
        try:
            with open("bd.atitus", "r") as arquivo:
                for linha in arquivo:
                    print(linha.strip())
        except FileNotFoundError:
            print("Nenhum aluno encontrado. Adicione alunos primeiro.")
        aguardar(5)
    else:
        print("Opção inválida. Tente novamente.")
        aguardar(2)