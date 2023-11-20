import time

class LRU:
    
    def executar(self, num_quadros:int, refs:list):         #recebe de parametro o num de quadros e as pags referenciadas
        tempo_inicial = time.time()

        page_faults = 0

        quadros = {} # a chave é o num da page e o valor é seu tempo na memoria principal

        for ref in refs:
            if ref not in quadros.keys():
                page_faults += 1
                if len(quadros) == num_quadros:
                    mais_antiga = self.__encontra_mais_antiga(quadros)
                    del quadros[mais_antiga]
                    print(f"a pagina {mais_antiga} foi removida da mem principal")
            quadros[ref] = 0 #se já tiver na mem, atualiza o tempo pra 0, se não tiver, adiciona na mem
            print(quadros.keys())
            print(quadros.values())
        
            for quadro in quadros:
                quadros[quadro] += 1
        
        tempo_final = time.time()
        tempo_execucao = tempo_final - tempo_inicial
        tempo_execucao = round(tempo_execucao, 4)

        print(f"Tempo de execução: {tempo_execucao} segundos")
        
        return page_faults


    
    def __encontra_mais_antiga(quadros):
        mais_antiga = list(quadros.keys())[0]
        for page in quadros.keys():
            if quadros[page] > quadros[mais_antiga]:
                print(f"A pagina {page} é a mais antiga com tempo igual a {quadros[page]}")
                mais_antiga = page
        return mais_antiga

lru = LRU

with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

lista_referencias = [linha.strip() for linha in linhas[1:]]
num_quadros = int(linhas[0].strip()) 
print(lista_referencias)

faults = lru.executar(lru, num_quadros, lista_referencias)
print(f"Houve {faults} page faults!")
