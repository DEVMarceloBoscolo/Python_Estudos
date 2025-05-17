
# print(type(booleano))

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# altura = float(input('Digite a sua altura: '))
# nome = input('Digite seu nome: ')
# idade = 24
# altura = 1.90
# booleano = True

# print(nome)

# print(type(nome))
# print(type(idade))
# print(type(altura
# print(nome)
# print(idade)
# print(altura)

# print(type(nome))
# print(type(idade))
# print(type(altura))

# idade = int(input('Digite sua idade: '))
# idade2 = int(input('Digite outra idade: '))

# media = (idade + idade2) / 2
# soma = idade + idade2
# subtracao = idade - idade2
# multplicacao = idade * idade2

# print(soma)
# print(media)
# print(subtracao)
# print(multplicacao)

# expon = 10 ** 3
# print(expon)

# inteira = 10 // 3

# print(inteira)

# resto = 10 % 3

# print(resto)

# nome = input('Digite seu nome: ')
# idade = int(input('Digite a sua idade: '))


# print(f'Bom dia {nome}, de idade {idade}')

nota1 = float(input('Digite a 1° nota: '))
nota2 = float(input('Digite a 2° nota: '))
nota3 = float(input('Digite a 3° nota: '))
nota4 = float(input('Digite a 4° nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'{media:.1f}')
 
nome:gabriel

salario_MES= float(input("digite seu salrio "))
horas_semana= float(input("digite quantas horas voce trabalha na semana "))
horas_mes= horas_semana*4
salrio_hora= salario_MES/horas_mes
print (horas_mes)
print (f"{salrio_hora:.2f}")
print(F"voce recebe {salrio_hora:.2f} por hora")



nome = Kleber-Lima

salario = float(input("digite o seu salário: "))
horas_trab = float(input("digite quantas horas você trabalhou: "))
val_hora = horas_trab * 4
print( f"valor da hora extra é: {val_hora:.2f}")
salar_hora = salario / val_hora 
print( f"O salário por hora é: {salar_hora:.2f}")


# Atividade revisão

# valor_hora = float(input('Digite a sua hora: '))
# horas_trabalhados = int(input('Digite a quantidade de horas no mês:'))

# calculo_salario = valor_hora * horas_trabalhados

# print(f'Salario do mês: {calculo_salario}')

# Aula 2
# Comparação
# x = 20
# y = 20
# igualdade = x == y
# maior = x > y
# maior_1 = x >= y
# diferente = x != y
# print(diferente)


# Operadores lógicos
# resultado1 = True
# resultado2 = False

# print(resultado1 and resultado2)
# print(resultado1 or resultado2)
# print(not resultado2)

# Operadores de atribuição
# x = 10
# x /= 2
# x += 10
# x = x + 10
# print(x)

# Operadores associação
# nome1 = 'Felipe'
# nome2 = 'Chico'
# nome3 = 'João'

# print('Tiago' not in (nome1, nome2, nome3))

# Atividade 1
# idade1 = int(input('Digite a primeira idade: '))
# idade2 = int(input('Digite a segunda idade: '))

# print(f'''
#       Idades iguais? {idade1==idade2}
#       Idade 1 é maior que idade 2? {idade1 > idade2}
#       Idade 2 é maior que idade 1? {idade2 > idade1}
# ''')

# Atividade 2
# palavra1 = input('Digite a 1° palavra: ')
# palavra2 = input('Digite a 2° palavra: ')

# print(f'São iguais: {palavra1==palavra2}')

# if 5 < 4:
#     print('Teste')
# elif 10 < 3:
#     print('Olá')
# elif 10 < 5:
#     print('Teste 2')
# else:
#     print('Caiu no else')

# Atividade 1 condicionais
# numero = int(input('Digite um número: '))

# if numero % 2 == 0:
#     print('Par')
# else:
#     print('Ímpar')

# Atividade 2
# nota = float(input('Digite uma nota: '))

# if nota >= 6:
#     print('Aprovado')
# else:
#     print('Reprovado')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 19.1:
    print('Abaixo do peso')
elif 19.1 <= imc < 25.8:
    print('Peso normal')
elif 25.8 <= imc < 27.3:
    print('Pouco acima do peso')
elif 27.3 <= imc < 32.3:
    print('Acima do peso')
else:
    print('Obesidade')

print(f'{imc:.2f}')
