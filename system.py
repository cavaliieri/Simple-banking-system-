from datetime import datetime

data_atual = datetime.now().date()
nome_cliente = input("Digite seu nome:")
saldo = 0
limite = 500
extrato = []
transacoes_feitas = 0
LIMITE_TRANSACOES_DIARIAS = 10

menu = f"""

---------- Seja Bem Vindo(a) {nome_cliente.upper()} ----------

Você gostaria de:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Ver saldo
[5] Sair

---------------------------------------------
Digite a opção desejada: """


def depositar():
    global saldo, transacoes_feitas
    if transacoes_feitas >= LIMITE_TRANSACOES_DIARIAS:
        print("Voce atingiu o limite de saques diarios")
        input("Pressione ENTER para continuar")
        return

    valor = float(input("Digite o valor que deseja depositar: "))

    if valor > 0:
        print(f"Você acabou de depositar R$:{valor:.2f}")
        saldo += valor
        transacoes_feitas += 1
        hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        extrato.append(f"{hora} Deposito R$ {valor:.2f}")
        input("Pressione ENTER para continuar")
    else:
        print("Valor invalido")


def sacar():
    global saldo, transacoes_feitas
    if transacoes_feitas >= LIMITE_TRANSACOES_DIARIAS:
        print("Voce atingiu o limite de saques diarios")
        input("Pressione ENTER para continuar")
        return
    valor = float(input("Digite o valor que deseja sacar:"))
    if valor > saldo:
        print("Saldo insuficiente")
        input("Pressione ENTER para continuar")
    elif valor > limite:
        print(f"O limite de saque é {limite}")
        input("Pressione ENTER para continuar")

    elif valor <= 0:
        print("Valor invalido")
        input("Pressione ENTER para continuar")
    else:
        saldo -= valor
        transacoes_feitas += 1
        hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"Voce acabou de realizar um saque de {valor:.2f} ")
        print(f"Seu saldo atual é de: R$:{saldo}")
        extrato.append(f"{hora} Voce fez um saque no valor de: {valor:.2f}")
        input("Pressione ENTER para continuar")


def ver_extrato():
    print("\n--------EXTRATO--------")

    if not extrato:
        print("Nenhuma movimentação encontrada")
        input("Pressione ENTER para continuar")
    else:
        for item in extrato:
            print(item)

        print(f"Saldo atual R$:{saldo:.2f}")
        input("Pressione ENTER para continuar")


def ver_saldo():
    print(f"Seu saldo atual é de R$:{saldo}")
    input("Pressione ENTER para continuar")


while True:
    if datetime.now().date() != data_atual:
        transacoes_feitas = 0
        data_atual = datetime.now().date()

    exibir_menu = input(menu)

    if exibir_menu == "1":
        depositar()

    elif exibir_menu == "2":
        sacar()
    elif exibir_menu == "3":
        ver_extrato()

    elif exibir_menu == "4":
        ver_saldo()

    elif exibir_menu == "5":
        print("Obrigado por usar nosso aplicativo")
        break

    else:
        print("Operação invalida, por favor selecione novamente a opção desejada")
