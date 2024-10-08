# # saber o salario da pessoa pelo ganho por hora e as horas trabalhadas mensalmente

# ganhoH = float(input("Quanto ganha por hora de trabalho?"))
# horasTrabalho = int(input("Quantas horas por mês?"))
# salario = ganhoH * horasTrabalho
# print(f"Seu salário mensal é: {ganhoH * horasTrabalho}")

## saber o imc de uma pessoa

# massa = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura (em M)"))
# imc = massa/(altura**2)

# print(f"seu IMC é = {imc:.2f}")

## Receber 2 notas e calcular a media entre as notas e checar se o aluno foi aprovado ou reprovado (media de aprovação 7)

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# media = (nota1 + nota2)/2

# if media >= 7:
#     print (f"Média= {media}, aprovado!")
# else:
#     print (f"Média= {media}, reprovado!")


## Checar se um número é par ou impar

# numero = int(input("Digite um numero: "))

# if (numero % 2 == 0):
#     print (f"O número {numero} é par")
# else:
#     print (f"O número {numero} é ímpar")


## Pedir a cor do semáforo e exibe uma mensagem respectiva para a cor escolhida:
## "pare" - vermelho; "atenção" - amarelo; "prossiga" - verde

# semaforo = input ("Digite a cor do semáforo: ").lower()

# if semaforo == "vermelho":
#     print("Pare")
# elif semaforo == "verde":
#     print ("Prossiga")
# elif semaforo == "amarelo":
#     print("Atenção")
# else:
#     print("Opção inválida!")


## Pedir a idade e saber se o voto é obrigatorio, possível e não pode.
## menos de 16 não pode; entre 16 e 17 ou maior que 70 facultativo; 18 até 70 obrigatório;

idade = int(input("Digite sua idade: "))

if (idade < 16 ):
    print("Não pode votar!")
elif (idade >= 16 and idade < 18 or idade >70):
    print("Voto Facultativo!")
else:
    print("Voto obrigatório!")