valor = float(input())

if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print("Deposito realizado com sucesso! \n Saldo atual: R$ " + "{:.2f}".format(valor))
elif valor == 0:
    #TODO: Imprimir a mensagem de valor inválido.
    print("Encerrando o programa...")
else:
    #TODO: Imprimir a mensagem de encerrar o programa.
    print("Valor invalido! Digite um valor maior que zero.")