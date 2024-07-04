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

# Loop principal do programa
while True:
    limparTela()
    print("(0) Sair")
    print("(1) Incluir Aluno")
    print("(2) Mostrar Lista")
    opcao = input()
    if opcao == "0":
        break # Encerra o loop e o programa
    elif opcao == "1":
        nome = input("Nome: ") # Captura o nome do aluno
        email = input("E-mail: ") # Captura o e-mail do aluno
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