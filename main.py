from funcoes import limparTela, aguardar

while True:
    limparTela()
    print("(0) Sair")
    print("(1) Incluir Aluno")
    print("(2) Mostrar Lista")
    print("(3) de")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome:")
        email = input("E-mail:")
        arquivo = open("bd.atitus", "w") #w write #r read #a append
        arquivo.write(nome+" "+email+")