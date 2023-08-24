#FOR
texto = input("Informe um texto")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ") #end=" ":exibe os resultados lado a lado

print() #adiciona uma quebra de linha

#FOR ELSE
#execulta no final do laço 
# Verificando se um número é primo
num = int(input("Digite um número: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} não é um número primo.")
        break
else:
    print(f"{num} é um número primo.")

#RANGE 

for numero in range(0,10):
    print(numero, end=" ")

for numero in range(0,51,5):
    print(numero, end=" ")

#WHILE
#executa o código até que determinada coisa aconteça 

opcao = -1 

while opcao != 0: 
    opcao = int(input( "[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao ==1:
        print("Sacando...")
    elif opcao ==2: 
        print("Exibindo o extrato...")

#usando o break:

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break #também pode ser substituído por continue, mas com cuidado
    print(numero)