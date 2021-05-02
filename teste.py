from getpass import getpass

print("Digite seu nome: ")
nome = input()

print("Digite sua senha: ")
senha = getpass()
print(nome + ', sua senha é : ' + senha)