import time

"CÓDIGO"

...
#Leitura arquivo de testes 1
with open('input_teste1.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 1
...

#Leitura arquivo de testes 2
with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 2
...