#Uso de tabela de páginas e bits presente/ausente
#Páginas presentes na memória (teriam o acesso normalmente)
#Páginas marcadas como ausente precisam ser carregadas

def fifo_page_replacement(frames, pages):
    page_table = {}  # Dicionário para representar a página e seu bit de presença
    page_queue = []  # Fila para manter a ordem das páginas

    page_faults = 0  # Contador de page faults

    for page in pages:
        if page not in page_table:  # Se a página não está na tabela de páginas
            if len(page_queue) < frames:  # Se ainda houver quadros disponíveis
                page_table[page] = 1  # Define o bit de presença como 1 (alocada)
                page_queue.append(page)  # Adiciona a página na fila
            else:
                # Remove a primeira página adicionada (FIFO)
                removed_page = page_queue.pop(0)
                page_table.pop(removed_page)  # Remove da tabela de páginas

                # Adiciona a nova página no final da fila e na tabela de páginas
                page_queue.append(page)
                page_table[page] = 1
                page_faults += 1  # Incrementa o contador de page faults

    return page_faults

# Exemplo de uso
quadros_disponiveis = 3
total_paginas = 10
paginas = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

page_faults_total = fifo_page_replacement(quadros_disponiveis, paginas)
print("Total de page faults gerados:", page_faults_total)

