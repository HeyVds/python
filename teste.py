# def checar_idade(nome, idade):
#   if idade>= 18:
#     return f"\nO(a) {nome} é maior de idade\n"
#   else:  
#     return f"\nO(a) {nome} é menor de idade\n"
# print (checar_idade("Victor", 18))

# def cumprimentar(nome, hora):
#   if hora <12 and hora >0:
#     print(f"\nBom dia, {nome}!\n")
#   elif hora <18:
#     print(f"\nBoa tarde, {nome}!\n")
#   elif hora <24:
#     print(f"\nBoa noite, {nome}!\n")
#   else:
#     print(f"\nDigita a hora certa otaro.\n")

# cumprimentar("Victor", 18)
# cumprimentar("Victor", 13)
# cumprimentar("Victor", 8)

# def cont_vogal():
#   palavra = input("Digite um nome: ")
#   vogal = "aeiou"
#   contador = 0
#   for i in palavra:
#     if i.lower() in vogal:
#       contador += 1
#   print(f"O nome {palavra}, tem {contador} vogal(is).")

# cont_vogal()

# notas = []
# while True:
#   menu = int(input("Digite 1 para digitar uma nota ou 2 para encerar: "))
#   if menu == 1:
#     nota = float(input("\n1Digite uma nota: "))
#     notas.append(nota)
#   elif menu == 2:
#     print("\nInserção de notas encerrada\n")
#     break
# def media_notas (notas):
#   media = 0
#   media = sum(notas)/len(notas)
#   if media >= 7:
#     return print(f"\nAluno aprovado com média {media}.\n")
#   else:
#     return print(f"\nAluno reprovado com média {media}.\n")

# print(media_notas(notas))



def conferir_senha(senha):
  tem_8_digitos = 0
  tem_minuscula = 0
  tem_maiuscula = 0
  tem_caracter = 0
  tem_numero = 0

  minuscula = "qwertyuiopasdfghjklçzxcvbnm"
  maiuscula = minuscula.upper()

  if len(senha)>= 8:
    tem_8_digitos = 1
  for caracter in senha:
    if caracter in minuscula:
      tem_minuscula = 1
    elif caracter in maiuscula:
      tem_maiuscula = 1
    elif caracter.isdigit():
      tem_numero = 1
    else:
      tem_caracter = 1
    
  requisitos = tem_8_digitos + tem_minuscula + tem_maiuscula + tem_numero + tem_caracter

  if requisitos <= 2:
    return "Senha fraca!"
  
  elif requisitos <= 4:
    return "Senha média!"
  
  else:
    return "Senha forte!"

print(conferir_senha("1AE!QWERo"))
