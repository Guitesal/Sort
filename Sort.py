# --------------------------------
# BUBBLE SORT

# A função bubbleSort realiza o algoritmo de ordenação Bubble Sort.
# Ela percorre a lista várias vezes, comparando elementos adjacentes e trocando-os se estiverem na ordem errada.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def bubbleSort(list):
    n = len(list)
    comparisons = changes = 0
    for i in range(n):
        for j in range(n - 1):
            comparisons += 1
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                changes += 2
    return list, comparisons, changes

# --------------------------------
# IMPROVED BUBBLE SORT

# A função improvedBubbleSort é uma variação otimizada do Bubble Sort.
# Ela utiliza uma flag para verificar se houve alguma troca durante uma passagem completa pela lista.
# Se não houver trocas, significa que a lista já está ordenada e o algoritmo pode parar.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def improvedBubbleSort(list):
    n = len(list)
    comparisons = changes = 0
    flag = True
    for i in range(n):
        if flag:
            flag = False
            for j in range(n - 1):
                comparisons += 1
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    changes += 2
                    flag = True
    return list, comparisons, changes

# --------------------------------
# SELECTION SORT

# A função selectionSort implementa o algoritmo Selection Sort.
# Ele divide a lista em uma parte ordenada e uma parte não ordenada.
# Em cada iteração, encontra o menor elemento da parte não ordenada e o troca com o primeiro elemento da parte não ordenada.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def selectionSort(list):
    n = len(list)
    comparisons = changes = 0
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            comparisons += 1
            if list[j] < list[menor]:
                menor = j
        comparisons += 1
        if list[i] != list[menor]:
            list[i], list[menor] = list[menor], list[i]
            changes += 2
    return list, comparisons, changes

# --------------------------------
# INSERTION SORT

# A função insertionSort implementa o algoritmo Insertion Sort.
# Ele constrói uma sequência ordenada, inserindo um elemento por vez da parte não ordenada na parte ordenada.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def insertionSort(list):
    comparisons = changes = 0
    for i in range(1, len(list)):
        chave = list[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and chave < list[j]:
            list[j + 1] = list[j]
            changes += 1
            j -= 1
        list[j + 1] = chave
        changes += 1
    return list, comparisons, changes

# --------------------------------
# INSERTION SORT COM BUSCA BINARIA

# A função buscaBinaria implementa a busca binária, utilizada no Insertion Sort com busca binária.
# Retorna a posição onde o elemento deve ser inserido.

def buscaBinaria(list, chave, ini, fim):
    comparisons = 0
    while ini <= fim:
        meio = (ini + fim) // 2
        comparisons += 1
        if list[meio] < chave:
            ini = meio + 1
        else:
            fim = meio - 1
    return ini, comparisons

# A função insertionSortBinary implementa o Insertion Sort com busca binária.
# Utiliza a busca binária para encontrar a posição correta de inserção de cada elemento.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def insertionSortBinary(list):
    comparisons = changes = 0
    for i in range(1, len(list)):
        chave = list[i]
        j = i - 1
        insert_idx, comp = buscaBinaria(list, chave, 0, j)
        comparisons += comp
        list[insert_idx + 1: j + 2] = list[insert_idx: j + 1]
        changes += (j - insert_idx + 1)
        list[insert_idx] = chave
    return list, comparisons, changes

# --------------------------------
# MERGE SORT

# A função mergeSort implementa o algoritmo Merge Sort.
# Divide a lista em partes menores, ordena-as e depois as mescla de volta em uma lista ordenada.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def mergeSort(list):
    comparisons = changes = 0
    def merge(left, right):
        nonlocal comparisons, changes
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                changes += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result
    stack = [(0, len(list))]
    while stack:
        start, end = stack.pop()
        if end - start < 2:
            continue
        mid = (start + end) // 2
        left = list[start:mid]
        right = list[mid:end]
        stack.append((start, mid))
        stack.append((mid, end))
        list[start:end] = merge(left, right)
    return list, comparisons, changes

# --------------------------------
# QUICK SORT

# A função quickSort implementa o algoritmo Quick Sort.
# Ele escolhe um elemento como pivô, e rearranja a lista de modo que os elementos menores que o pivô fiquem à esquerda, e os maiores à direita.
# Utiliza uma pilha para simular a recursão do algoritmo.
# Retorna a lista ordenada, o número de comparações e o número de trocas realizadas.

def quickSort(list):
    stack = [(0, len(list) - 1)]
    comparisons = changes = 0
    while stack:
        left, right = stack.pop()
        while left < right:
            pivot = list[right]
            i = left - 1
            for j in range(left, right):
                comparisons += 1
                if list[j] <= pivot:
                    i += 1
                    list[i], list[j] = list[j], list[i]
                    changes += 2
            list[i + 1], list[right] = list[right], list[i + 1]
            changes += 2
            if i - left < right - i:
                stack.append((left, i))
                left = i + 2
            else:
                stack.append((i + 2, right))
                right = i
    return list, comparisons, changes

# --------------------------------
# BUCKET SORT

# A função bucketSort implementa o algoritmo Bucket Sort.
# Divide a lista em "buckets" e os ordena individualmente.
# Depois, concatena os buckets ordenados para obter a lista final ordenada.

def bucketSort(list):
    min_value = min(list)
    max_value = max(list)
    num_buckets = max_value - min_value + 1
    buckets = [[] for _ in range(num_buckets)]
    for num in list:
        index = num - min_value
        buckets[index].append(num)
    index = 0
    for i in range(num_buckets):
        if len(buckets[i]) > 0:
            buckets[i].sort()
            for j in range(len(buckets[i])):
                list[index] = buckets[i][j]
                index += 1
    return list, 0, 0

# --------------------------------
# COUNTING SORT

# A função countingSort implementa o algoritmo Counting Sort.
# Conta a frequência de cada elemento e utiliza essa informação para ordenar a lista.
# Retorna a lista ordenada e o número de comparações realizadas.

def countingSort(list):
    max_value = max(list)
    counts = [0] * (max_value + 1)
    for num in list:
        counts[num] += 1
    comparisons = 0
    index = 0
    for i in range(len(counts)):
        comparisons += 1
        while counts[i] > 0:
            list[index] = i
            index += 1
            counts[i] -= 1
    return list, comparisons, 0

# --------------------------------

# arr = [3,8,2,5,9,2,10]
# print(f"Bubble Sort: {bubbleSort(arr)}")
# print(f"Improved Bubble Sort: {improvedBubbleSort(arr)}")
# print(f"Selection Sort: {selectionSort(arr)}")
# print(f"Insertion Sort: {insertionSort(arr)}")
# print(f"Insertion Sort (Binary): {insertionSortBinary(arr)}")
# print(f"Merge Sort: {mergeSort(arr)}")
# print(f"Quick Sort: {quickSort(arr)}")
# print(f"Bucket Sort: {bucketSort(arr)}")
# print(f"Counting Sort: {countingSort(arr)}")
