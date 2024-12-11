#Escreva uma função que receba uma lista de números e um valor inteiro n, e retorne uma nova lista com os n primeiros valores da lista original.
lista = []
while True:
  menu = int(input("\nDigite 1 para adicionar à lista ou 2 para parar: "))
  if menu == 1:
    numero = float(input("Digite um número para ser adicionado a lista: "))
    lista.append(numero)
  elif menu == 2:
    print("Inserção encerrada.")
    break
def mudar_lista(lista):
  nova_lista = []
  while True:
    n = int(input("\nDigite a quantidade de valores da nova lista: "))
    if n > len(lista):
      print(f"Digite um valor abaixo de {len(lista)+1}")
    else:
      break
  for i in range(n):
    nova_lista.append(lista[i])
  return print(f"\nA nova lista é: {nova_lista}")

mudar_lista(lista)