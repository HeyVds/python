#Crie um programa principal que importe um arquivo de módulo com as funções dos exercícios anteriores e utilize-as para realizar as seguintes operações: calcular a média de uma lista de números, imprimir a tabuada de um número informado pelo usuário e imprimir os valores de uma lista de números que são maiores que um valor informado pelo usuário.
import main

while True:
  menu = int(input("""
    Digite 1 para Calcular a média de uma lista de números:
    Digite 2 para Tabuada de um número:
    Digite 3 para Gerar uma lista de números que são maiores que o valor informado pelo usuário:
    Digite 4 para encerrar:
    """))
  match menu:
    case 1:
      lista = []
      while True:
        menu2 = int(input("\nDigite 1 para adicionar à lista ou 2 para parar: "))
        if menu2 == 1:
          numero = float(input("Digite um número para ser adicionado a lista: "))
          lista.append(numero)
        elif menu2 == 2:
          print("\nInserção encerrada.")
          break
      print(f"A média da lista criada com os valores acima é: {main.media_lista(lista)}")
    case 2:
      numero = int(input("\nDigite o número da tabuada: "))
      main.tabuada(numero)

    case 3:
        valor = int(input("\nDigite um valor: "))
        print(f"A lista com os números maiores que o valor informado: {main.lista_maiores_valores(valor)}")
    case 4:
        print("\nPrograma encerrado!")
        break
    case _:
        print("Digite um valor válido!")