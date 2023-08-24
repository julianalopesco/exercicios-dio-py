#IDENTAÇÃO 

def sacar (valor) -> None: #inicio do bloco do método 
    saldo = 500

    if saldo >= valor: #início do bloco do if 
        #fim do bloco do if
        print("valor sacado!")
#fim do bloco do método 
    print("Obrigado e volte sempre!")
    #está fora do bloco if e sempre executa 

sacar(100) 
#chamando o método 

#ESTRUTURAS CONDICIONAIS

#if
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

if saldo < saque: 
    print("Saldo insuficiente")

#if/else
saldo = 3000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque: 
    print("Realizando saque!")

else:
    print("Saldo insuficiente")

#elif 
import sys 
opcao = int(input("Informe uma opção:\n[1] Sacar\n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque:"))

elif opcao == 2:
    print("Exibindo o extrato...")
else: 
    sys.exit("Opção inválida")

#if aninhado
conta_normal = True
conta_universitaria = False 

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial")
    else: 
        print("Não foi possível realizar o saque, saldo insuficiente ")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else: 
        print("Saldo insuficiente")

print("#if ternário") 
saldo = 2000
saque = 50000

status = "Sucesso" if saldo >= saque else "Falha"
#se a condição do if for atendida, retornar o primeiro valor para a variável
print(f"{status} ao realizar o saque!")