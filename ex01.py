#Escreva uma função que receba uma lista de números e retorne o valor mínimo encontrado.
lista = []
while True:
  menu = int(input("\nDigite 1 para adicionar à lista ou 2 para parar: "))
  if menu == 1:
    numero = float(input("Digite um número para ser adicionado a lista: "))
    lista.append(numero)
  elif menu == 2:
    print("\nInserção encerrada.")
    break

def menor_valor(valores):
  menor_valor = valores[0]
  for i in valores:
    if i < menor_valor:
      menor_valor = i
  return print(f"O menor número listado foi: {menor_valor}")

menor_valor(lista)