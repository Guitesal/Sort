from random import sample
from Sort import bubbleSort, bucketSort, countingSort, improvedBubbleSort, selectionSort, insertionSort, insertionSortBinary, mergeSort, quickSort
from time import time

def salvar_resultados(nome_arquivo, resultados):
    with open(nome_arquivo, 'w') as file:
        for resultado in resultados:
            file.write(resultado)
            file.write('\n')

def main():
    algoritmos = [
        bubbleSort, improvedBubbleSort, selectionSort, insertionSort, insertionSortBinary,
        mergeSort, quickSort, bucketSort, countingSort
    ]

    listas = [
        ("Caso Ideal 1k", list(range(0,1000))),
        ("Caso Ideal 10k", list(range(0,10000))),
        ("Caso Ideal 100k", list(range(0,100000))),
        ("Caso Intermediário 1k", sample(range(0,1000), 1000)),
        ("Caso Intermediário 10k", sample(range(0,10000), 10000)),
        ("Caso Intermediário 100k", sample(range(0,100000), 100000)),
        ("Caso Ruim 1k", list(range(999, -1, -1))),
        ("Caso Ruim 10k", list(range(9999, -1, -1))),
        ("Caso Ruim 100k", list(range(99999, -1, -1))),
        # ("Caso Teste", list(range(49, -1, -1)))
    ]

    resultados = []

    for lista_nome, lista in listas:
        for algoritmo in algoritmos:
            arr_copy = lista[:]
            start_time = time()
            ordered, comparisons, changes = algoritmo(arr_copy)
            end_time = time()
            print(f"{algoritmo.__name__.upper()} - {lista_nome}")
            resultados.append(f"{algoritmo.__name__.upper()} - {lista_nome}")    
            # resultados.append(f"Lista ordenada: {ordered}")
            resultados.append(f"Número de trocas: {changes}")
            resultados.append(f"Número de comparações: {comparisons}")
            resultados.append(f"Tempo de execução: {round(end_time - start_time, 5)}")
            resultados.append("\n")

    salvar_resultados("Python\Paradigmas de Programação e Análise de Algoritmos\Projeto\Resultados.txt", resultados)

if __name__ == "__main__":
    main()
