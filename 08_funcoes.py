def exibir_mensagem():
    print("Olá mundo!")

#de f: informa que o exibir_mensagem é o nome de uma função
#função sem parâmetros

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
#recebe um argumento

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
#se o argumento não é passado, ele usa o padrão declarado

#executando as funções: 
exibir_mensagem()
exibir_mensagem_2(nome="Juliana")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

#Função de primeira classe: 

def somar(a, b):
    return a + b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a, b) 
    print (f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)