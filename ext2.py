nome = input("digite seu nome:")
print(nome)
senha = input("digite sua Senha:")
print(senha)

if nome == "admin" and senha == "123456":
    print('acesso permitido ')
else:
    print('acesso negado')