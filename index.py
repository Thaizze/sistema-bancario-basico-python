MENU = '''
    MENU:
    [s] - Sacar Dinheiro
    [d] - Depósito
    [e] - Extrato
    [x] - Sair
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print('*** Caixa eletrônico 24h ***')
usuario = input("Digite o seu nome: ")
print(f"Bem vindo(a) ao caixa 24h {usuario}!")

while True:   
    print(MENU)    
    opcao = input("Digite a opção desejada: ")

    if opcao == 's':  
        if saldo == 0:
            print(f"Você não possui saldo sulficiente para esta operação! Seu saldo atual é de R$ {saldo}")
        else:
            valor_saque = float(input("Digite o valor que você deseja sacar: "))
            excedeu_saldo = valor_saque > saldo
            excedeu_limite = valor_saque > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print(f"Você não possui saldo sulficiente para esta operação! Seu saldo atual é de R$ {saldo}")  
            elif excedeu_limite:
                print("O valor do saque excedeu o seu limite diário!")
            elif excedeu_saques:
                print("Você excedeu o seu limite diário de saques!")
            elif valor_saque > 0:              
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                print(f"Saque realizado com sucesso! Seu novo saldo é de R$ {saldo}")               
            else:
                print("O valor informado para saque é inválido!")
    elif opcao == 'd':
        deposito = float(input("Digite o valor que você deseja depositar:"))                 
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depóstio realizado com sucesso! Seu novo saldo é de R$ {saldo}")  
        else:            
            print("Valor inválido! O valor do depósito deve ser maior que R$ 0") 
    elif opcao == 'e':
        print("*** Extrato ***")
        print("Não foram realizadas movimentações na conta!" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == 'x':  
        print("Obrigado por utilizar o Caixa 24H! Volte Sempre!") 
        break 
    else:
        print("Opção inválida, por favor selecione novamente uma das opções do menu")
        print(MENU)
                

        