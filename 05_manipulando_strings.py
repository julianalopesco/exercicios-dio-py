#MANIPULANDO STRINGS

curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())
#altera a capitalização 

curso = "    Python  "
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
#remove espaços em branco

#INTERPOLAÇÃO DE VARIÁVEIS

nome = "juliana"
idade = 28
profissao = "Estagiaria"
linguagem = "Java"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}")

#fornatar string com f-string

PI = 3.14159 

print(f"Valor de PI: {PI: .2f}")