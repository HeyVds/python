lista = []
for i in range(5):
    marca = input("\nDigite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))
    cor = input("Digite a cor do carro: ")
    preco = float(input("Digite o preço do carro: "))

    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "cor": cor,
        "preço": preco
    }
    lista.append(carro)

carroMaisCaro = lista[0]
carroMaisBarato = lista[0]
qtdCarrosNovos = 0
valorTotal = 0

for car in lista:
    if car["preço"] > carroMaisCaro["preço"]:
        carroMaisCaro = car
    
    if car["preço"] < carroMaisBarato["preço"]:
        carroMaisCaro = car

    if car["ano"] > 2020:
        qtdCarrosNovos += 1
    
    valorTotal += car["preço"]

print(f"\nCarro mais caro: {carroMaisCaro['marca']}, {carroMaisCaro['modelo']}, R${carroMaisCaro['preço']}")
print(f"\nCarro mais barato: {carroMaisBarato['marca']}, {carroMaisBarato['modelo']}, R${carroMaisBarato['preço']}")
print(f"\nA qtd de carros com ano depois de 2020 são: {qtdCarrosNovos}.")
print(f"\nO Valor total de todos os carros: R${valorTotal}")