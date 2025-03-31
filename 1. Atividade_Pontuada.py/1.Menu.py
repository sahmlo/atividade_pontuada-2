import os
os.system("clear")

soma = 0
preco = 0
forma_de_pagamento = 0
subtotal = 0


print("Gourmet Tech")

while True:
    opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Carne do Sol \t\t R$ 25,00
2 \t Almôndegas \t\t R$ 22,00
3 \t Filé Grelhado \t\t R$ 18,00
4 \t Bisteca \t\t R$ 18,00
5 \t Filé de Tilápia \t R$ 22,00
6 \t Parmegiana \t\t R$ 26,00
7 \t Camarão à Milanesa \t R$ 43,00
0 \t Finalizar Pedido
                    
Digite a opção desejada: """))
    if opcao == 0:
        print(f"\nPedido encerrado. O valor total é R$ {soma:.2f}")
        break
    
    match opcao:
        case 1:
            prato = "Carne do Sol"
            preco = 25
        case 2:
            prato = "Almôndegas"
            preco = 22
        case 3:
            prato = "Filé Grelhado"
            preco = 18
        case 4:
            prato = "Bisteca"
            preco = 18
        case 5:
            prato = "Filé de Tilápia"
            preco = 22
        case 6:
            prato = "Parmegiana"
            preco = 26
        case 7:
            prato = "Camarão à Milanesa"
            preco = 43
        case _:
            print("\nOpção Inválida")
            preco = 0

    soma += preco
    subtotal += preco

    continuar = input("Deseja informa outro prato? (S/N): ").lower()
    if continuar == "n":
        break
while True:
        forma_de_pagamento = input('\nInforme a forma de pagamennto. \n1 - à vista (10% de desconto). \n2 - Cartão de credito (10% de acréscimo). \nInfome a opção escolhida: ')

        if forma_de_pagamento == "1":
            desconto_ou_acrescimo = subtotal * 0.10
            soma -= desconto_ou_acrescimo
            print("Desconto de 10% aplicado.")
            break
        elif forma_de_pagamento == "2":
            desconto_ou_acrescimo = subtotal * 0.10
            soma += desconto_ou_acrescimo
            print("Acréscimo de 10% aplicado.")
            break
        else:
            print("Opção inválida, tente novamente.")
