#OPERADORES ARITIMÉTICOS 

print(1+0)
print(2*1)
print(12/4)
print(100//25)
#divisão inteira
print(23%6)
#resto da divisão 

#OPERADORES DE COMPARAÇÃO 
#trazem valores booleanos

saldo = 450
saque = 200 
limite = 100

print(saldo == saque)
print(saldo != saque)
print(saldo >= saque)
print(saldo <= saque)

#OPERADORES DE ATRIBUIÇÃO

saldo_atrib = 500
#atribuição simples 
saldo_atrib += 200
print(saldo_atrib)

#OPERADORES LÓGICOS 

print(saldo >= saque and saque <= limite) 
print(saldo >= saque or saque <= limite) 

print(not 1000 > 1500)
#not contatos_emergencia
#operador de negação 

#OPERADORES DE IDENTIDADE

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200 

print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)

#OPERADORES DE ASSOCIAÇÃO

loja = "Quitanda do Seu Jorge"
frutas = ["laranja", "uva", "melancia"]
saques = [1500, 100]

print("Jorge" in loja)
#é case sensitive 
print("maçã" not in frutas)
print(200 in saques)