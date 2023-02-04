menu = '''
########## SISTEMA BANCÁRIO ###########
1 - Sacar | 2 - Depositar | 3 - Extrato
############# 0 - sair ################
Escolha uma opção: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        print("### Saque ###")
        valor = float(input("Digite o valor do saque: $"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if (excedeu_saldo):
            print("A operação falhou pois você não tem saldo suficiente.")

        elif (excedeu_limite):
            print("A operação falhou pois excedeu do limite de saque.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Digite um valor válido.")

    elif opcao == 2:
        print("\n\n### Deposito ###")
        valor = float(input("Digite o valor do depósito: $"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
        else:
            print("O valor informado é inválido.")


    elif opcao == 3:
        print("### Extrato ###")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("###############")

    elif opcao == 0:
        menu = 0 #0 é false, mudando o menu pra 0 coloca ele como false, parando o while, também poderia usar 'break'

    else:
        print("Por favor, escolha uma opção válida")