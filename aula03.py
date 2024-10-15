# contador = 1

# while contador <= 10:
#     print(f"O contador é {contador}")
#     contador +=1
# print ("Acabou aqui parsa!")


## ex02
# Faça um loop de rep que mostra todos os números entre o 7 e 29:

# contador = 7

# while contador < 29:
#     print(contador)
#     contador += 1


## pedir idade para 10 pessoas e calcular a media das idades

# contador = 1
# somaIdades = 0

# while contador < 11:
#     idade = int(input("Digite sua idade: "))
#     somaIdades += idade
#     contador += 1

# media = somaIdades/10

# print(f"a media das idades é {media:.0f}")

## digitar 8 números e mostrar se ele é par ou impar

# contador = 1

# while contador <=8:
#     numero = float(input("Digite um número: "))
#     if numero % 2 == 0:
#         print(f"o número {numero} é par")
#     else:
#         print(f"o número {numero} é impar")
#     contador +=1


## while True

# while True:
#     menu = input("Digite 1 para cadastrar ou 2 para sair: ")
#     if menu == "1":
#         produto = input("Digite o nome do produto: ")
#     elif menu == "2":
#         print ("Fim do programa")
#         break
#     else:
#         print("Opção inválida! Tente novamente.")


## pedir um numero indeterminado de notas e decidir quando parar, e no final exibir a média das notas

# contador = 1
# soma = 0
# while True:
#     nota = int(input("Digite a nota da vez: "))
#     soma += nota
#     menu = int(input("Digite 2 para parar de adicionar notas:"))
#     if menu == 2:
#         break
#     else:
#         print("Próxima nota")
#     contador += 1

# media = soma/contador

# print(f"A média das {contador} notas resultou em: {media}")


## pedir um numero indeterminado de idades e mostrar a maior ao parar o programa

maiorIdade = 0

while True:
    menu = int(input("Escolha uma opção: 1 para adicionar 2 para parar."))
    if menu == 1:
        idade = int(input("Digite a idade do convidado da vez: "))
        if idade > maiorIdade:
            maiorIdade = idade
    elif menu == 2:
        break
    else:
        print("Opção inválida!")

print(f"A maior idade é : {maiorIdade}")