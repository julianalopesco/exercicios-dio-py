print(5//2)

#USANDO VARIÁVEIS E CONSTANTES:

#VARIÁVEIS:
age = 28
name = 'Juliana'

print(f'Meu nome é {name} e eu tenho {age} anos de idade')

#f-strings: formata as saídas 

age = 30
nome_completo = 'Afonso Poncho'

nome, idade = ('Matheus', 25)

print(nome, idade)

print(f'Meu nome é {name} e eu tenho {age} anos de idade')

#CONSTANTES: 

ESTADOS = ['SP', 'RJ', 'MG']

print(ESTADOS)

#CONVERSÃO DE TIPOS:

preco = 10.50 
idade = 28 

print(str(preco))
print(str(idade)) 
#str:  construtor

texto = f"idade {idade} preco {preco}"
print(texto)

print(float(100)) 
#no console sai 100.0

#INPUT E OUTPUT 

nome_input = input("Informe seu nome: ")
print(nome_input)