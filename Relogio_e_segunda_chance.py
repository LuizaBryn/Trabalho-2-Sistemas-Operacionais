import time

def relogio(num_quadros, lista_referencias):
    tempo_inicial = time.time()

    page_faults = 0
    ...
    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    tempo_execucao = round(tempo_execucao, 4)

    print(f"Tempo de execução: {tempo_execucao} segundos")

    return page_faults

#Leitura arquivo de testes 1
with open('input_teste1.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 1
page_faults = relogio(num_quadros, lista_referencias)
print(f"Houve {page_faults} page faults!")

#Leitura arquivo de testes 2
with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 

#TESTE 2
page_faults = relogio(num_quadros, lista_referencias)
print(f"Houve {page_faults} page faults!")