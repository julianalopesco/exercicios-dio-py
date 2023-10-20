# sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. 
#Os ativos são representados por strings que representam seus tipos, 
#como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

ativos = []
# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

#ex input: Financiamento de Imovel, Deposito, Reservas Bancarias

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
    print(ativo)
