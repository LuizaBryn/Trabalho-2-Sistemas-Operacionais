class LRU:
    
    def executar(self, num_quadros:list, refs:list):         #recebe de parametro o num de quadros e as pags referenciadas

        page_faults = 0

        quadros = {}

        for ref in refs:
            if ref not in quadros.keys():
                page_faults += 1
                if len(quadros) == num_quadros:
                    self.deleta_mais_antiga(quadros)
            quadros[ref] = 0 #se já tiver na mem, atualiza o tempo pra 0, se não tiver, adiciona na mem
        
        for quadro in quadros:
            quadros[quadro] += 1
        

    
    def deleta_mais_antiga(quadros):
        pass
