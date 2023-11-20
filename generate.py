import random

# Geração de números distintos aleatórios no intervalo de 0 a 500
distinct_numbers = random.choices(range(0, 500), k=100000)

# Escrita dos números no arquivo de entrada
with open('input_teste2.txt', 'w') as file:
    file.write("64\n")  # Escreve o número de blocos (64) na primeira linha
    for number in distinct_numbers:
        file.write(f"{number}\n")  # Escreve os números de página distintos
