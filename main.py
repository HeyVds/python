import random

#calcular a média de uma lista de números
def media_lista(lista_numeros):
  media = sum(lista_numeros)/len(lista_numeros)
  return media

#imprimir a tabuada de um número informado pelo usuário
def tabuada(numero):
  for multiplicador in range(11):
    print(f"{multiplicador} x {numero} = {multiplicador * numero}")
  
#imprimir os valores de uma lista de números que são maiores que um valor informado pelo usuário
def lista_maiores_valores(valor):
  novos_valores = []
  for i in range(10):
    novo_valor = random.randint(valor, valor+100) 
    novos_valores.append(novo_valor)
  return novos_valores