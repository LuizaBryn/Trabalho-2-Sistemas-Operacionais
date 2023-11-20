def fifo_page(blocos, paginas):
    tab_pag = {}  # Dicionário para representar a página e seu bit de presença
    pag_fila = []  # Fila para manter a ordem das páginas

    page_faults = 0  # Contador de page faults

    for pag in paginas:
        pag = int(pag)
        if pag not in tab_pag:  # Se a página não está na tabela de páginas
            if len(pag_fila) < blocos:  # Se ainda houver blocos disponíveis
                tab_pag[pag] = 1  # Define o bit de presença como 1 (alocada)
                pag_fila.append(pag)  # Adiciona a página na fila
            else:
                # Remove a primeira página adicionada (FIFO)
                pag_removida = pag_fila.pop(0)
                tab_pag.pop(pag_removida)  # Remove da tabela de páginas

                # Adiciona a nova página no final da fila e na tabela de páginas
                pag_fila.append(pag)
                tab_pag[pag] = 1
                page_faults += 1  # Incrementa o contador de page faults

    return page_faults

# Leitura do arquivo de entrada
with open('input_teste2.txt', 'r') as file:
    linhas = file.readlines()

blocos = int(linhas[0].strip())  # Primeira linha contém o número de blocos
paginas = [linha.strip() for linha in linhas[1:]]  # Restante das linhas são as páginas

page_faults_total = fifo_page(blocos, paginas)
print("Total de page faults gerados:", page_faults_total)

