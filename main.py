operacoes = dict()
saldo = 1000
saques = 0
depositos = 0

while True:
    menu = f'''
====================================
Banco Central

Menu de opções

1 - Depósito
2 - Saque
3 - Extrato
4 - Sair

Saldo: R${saldo:.2f}
====================================

Opção: 
'''
    
    opcao = int(input(menu))
    print("")

    match opcao:
        case 1:
            print("---------------")
            print("Menu de Depósitos")
            print("---------------")

            valor = float(input("\nValor: R$"))

            saldo = saldo + valor

            depositos = depositos + 1

            operacoes[f'deposito-{depositos}'] = f"{valor:.2f}"
        case 2:
            print("---------------")
            print("Menu de Saques")
            print("---------------")

            if (saques == 3):
                print("Você atingiu o limite de saque diário.")
                continue

            valor = float(input("\nValor: R$"))

            if (valor > saldo):
                print("Saldo insuficiente.")
                continue

            while (valor > 500):
                valor = float(input("Insira um valor menor que R$500. Valor: R$"))
            
            saldo = saldo - valor

            saques = saques + 1

            operacoes[f'saque-{saques}'] = f"{valor:.2f}"
        case 3:
            print("---------------")
            print("Extrato bancário")
            print("---------------\n")

            for chave, valor in operacoes.items():
                print(f"Operação: {chave.capitalize()}: R${valor}")
        case 4:
            break
        case _:
            print("\nOpção inválida")

print("\nEncerrado.")

