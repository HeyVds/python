biblioteca = []
print("\nBem vindo a biblioteca.")
while True:
    menu = input("\nDigite 1 para cadastrar livros, 2 para ver livros ou qualquer tecla para sair: ")
    if menu == "1":
        titulo = input("\nDigite o Tílulo do livro: ")
        genero = input("Digite o gênero do livro: ")
        preco = float(input("Digite o preço do livro: "))

        novoLivro = {
            "titulo": titulo,
            "genero": genero,
            "preço": preco
        }
        biblioteca.append(novoLivro)
    elif menu == "2":
        for livro in biblioteca:
            print(f"Livro: {livro['titulo']}, gênero: {livro['genero']}, preço: {livro['preco']}")
    else:
        break