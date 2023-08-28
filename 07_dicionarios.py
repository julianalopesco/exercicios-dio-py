#DECLARANDO DICIONÁRIOS: 

#Forma 01: 
pessoa = {"nome": "Guilherme", "idade":28} #declaraçaõ da variável pessoa que recebe um dicionário
#chave:valor 

#Forma 02:
pessoa = dict(nome="Guilherme", idade=28)
#dict: classe construtora

#Adicionando nova chave em um dicionário já existente 
pessoa["telefone"] = "3333-1234"

#Dicionários aninhados: 

contatos = { 
    "maria@gmail.com" : {"nome": "Maria", "telefone": "3333-5151"},
    "alberto@gmail.com" : {"nome": "Alberto", "telefone": "7333-5158"},
    "joaquim@gmail.com" : {"nome": "Joaquim", "telefone": "3348-5751"},
    "manoel@gmail.com" : {"nome": "Manoel", "telefone": "7895-5787"},
    #dentro de cada registro no dicionário, há um dicionário com os dados do registro
}

telefone = contatos ["maria@gmail.com"] ["telefone"]
print(telefone)
#acessando dados do dicionário

#Iterando dicionários:

for chave in contatos:
    print(chave, contatos[chave])
    #imprime o valor da chave, e o dicionário

for chave, valor in contatos.items():
    print(chave, valor)