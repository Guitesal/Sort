from random import sample
from Sort import bubbleSort, bucketSort, countingSort, improvedBubbleSort, selectionSort, insertionSort, insertionSortBinary, mergeSort, quickSort
from time import time

def print_sort():
    print("Escolha um algoritmo de ordenação:")
    print("1. Bubble Sort")
    print("2. Improved Bubble Sort")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    print("5. Insertion Sort + Binary Search")
    print("6. Merge Sort")
    print("7. Quick Sort")
    print("8. Bucket Sort")
    print("9. Counting Sort")
    print("0. Sair")


def print_list():
    print("Escolha a lista para ser ordenada:")
    print("1. Caso Ideal - 1k")
    print("2. Caso Ideal - 10k")
    print("3. Caso Ideal - 100k")
    print("4. Caso Intermediário - 1k")
    print("5. Caso Intermediário - 10k")
    print("6. Caso Intermediário - 100k")
    print("7. Caso Ruim - 1k")
    print("8. Caso Ruim - 10k")
    print("9. Caso Ruim - 100k")
    print("10. TESTE")
    print("0. Sair")


def run_sort(sortFunction, arr_copy, functionTitle, arrTitle):
    start_time = time()
    ordered, comparisons, changes = sortFunction(arr_copy)
    end_time = time()

    execution_time = round(end_time - start_time, 3)
    print(f"{functionTitle} - {arrTitle}")
    # print(f"Lista ordenada: {ordered}")
    print(f"Número de trocas: {changes}")
    print(f"Número de comparações: {comparisons}")
    print(f"Tempo de execução: {execution_time}")
    print("\n")

def main():
    flag = False
    arr = []
    while True:
        if flag == False:
            print_list()
            listChoice = input("Digite o número da lista desejada: ")
            print("\n")
            if listChoice == "0":
                break
            elif listChoice == "1":
                arrTitle = "Caso Ideal 1k"
                arr = list(range(0, 1000))
            elif listChoice == "2":
                arrTitle = "Caso Ideal 10k"
                arr = list(range(0, 10000))
            elif listChoice == "3":
                arrTitle = "Caso Ideal 100k"
                arr = list(range(0, 100000))
            elif listChoice == "4":
                arrTitle = "Caso Intermediário 1k"
                arr = sample(range(0, 1000), 1000)
            elif listChoice == "5":
                arrTitle = "Caso Intermediário 10k"
                arr = sample(range(0, 10000), 10000)
            elif listChoice == "6":
                arrTitle = "Caso Intermediário 100k"
                arr = sample(range(0, 100000), 100000)
            elif listChoice == "7":
                arrTitle = "Caso Ruim 1k"
                arr = list(range(999, -1, -1))
            elif listChoice == "8":
                arrTitle = "Caso Ruim 10k"
                arr = list(range(9999, -1, -1))
            elif listChoice == "9":
                arrTitle = "Caso Ruim 100k"
                arr = list(range(99999, -1, -1))
            elif listChoice == "10":
                arrTitle = "Caso Teste"
                arr = list(range(49, -1, -1))
            else:
                break
            flag = True
        arr_copy = arr[:]
        print_sort()
        sortFunction = input("Digite o número da função desejada: ")
        print("\n")
        if sortFunction == "0":
            break
        elif sortFunction == "1":
            functionTitle = "BUBBLE SORT"
            run_sort(bubbleSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "2":
            functionTitle = "IMPROVED BUBBLE SORT"
            run_sort(improvedBubbleSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "3":
            functionTitle = "SELECTION SORT"
            run_sort(selectionSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "4":
            functionTitle = "INSERTION SORT"
            run_sort(insertionSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "5":
            functionTitle = "INSERTION SORT w/ BINARY SEARCH"
            run_sort(insertionSortBinary, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "6":
            functionTitle = "MERGE SORT"
            run_sort(mergeSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "7":
            functionTitle = "QUICK SORT"
            run_sort(quickSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "8":
            functionTitle = "BUCKET SORT"
            run_sort(bucketSort, arr_copy, functionTitle, arrTitle)
        elif sortFunction == "9":
            functionTitle = "COUNTING SORT"
            run_sort(countingSort, arr_copy, functionTitle, arrTitle)
        else:
            break
        loop = " "
        while loop != "S" and loop != "N":
            loop = input("Deseja mudar a lista de origem (S/N): ")
        if loop == "S":
            flag = False

main()