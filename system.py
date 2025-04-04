nome_cliente = input("Digite seu nome:")
saldo = 0
limite = 500
extrato = []
saques_feitos = 0
LIMITE_SAQUES = 3

menu = f''' 


---------- Seja Bem Vindo(a) {nome_cliente.upper()} ----------

Você gostaria de:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Ver saldo
[5] Sair

---------------------------------------------
Digite a opção desejada: '''


while True:  
    exibir_menu = input(menu)
    
    if exibir_menu == '1':
        print("Deposito")
        valor_depositado = float(input("Qual valor deseja depositar:"))
        
        if valor_depositado > 0:
            print(f'Você acabou de depositar R$:{valor_depositado:.2f}')
        else:
            print("Você não pode depoistar um valor negativo")

        saldo =+ valor_depositado
        extrato.append(f"Voce fez um deposito de {valor_depositado:.2f}")  
        print(f'{saldo:.2f}')
        print(extrato)
        input("Pressione enter para continuar")
        
       
        
  
    
    elif exibir_menu == '2':
        print("Sacar")
        valor_sacado = float(input("Qual valor você deseja sacar:"))
        if LIMITE_SAQUES >= saques_feitos and valor_sacado <= limite and valor_sacado <= saldo:
            print(f"Voce acabou de realizar um saque de {valor_sacado:.2f} ")
            extrato.append(f"Voce fez um saque no valor de: {valor_sacado:.2f}")
            saldo -= valor_sacado
            saques_feitos +=1
        else:
            print("Voce atingiu o limite de saques diarios ou excedeu o valor permitido")

        
        input("Pressione enter para continuar")
        
       
    
    elif exibir_menu == '3':
        print("Extrato")
        print(f'Aqui esta o seu extrato com suas ultimas atividades: {extrato} e o seu saldo atual é de {saldo:.2f}')
        input("Pressione enter para continuar")

    elif exibir_menu == '4':
        print(saldo)
        input("Pressione enter para continuar")


    
    elif exibir_menu == '5':
        print("Obrigado por usar nosso aplicativo")
        break

    else:
        print("Operação invalida, por favor selecione novamente a opção desejada")

