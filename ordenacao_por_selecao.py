def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordencao_por_selecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

arr = [5, 4, 6, 2, 10, 0.5, 3, 7, 23]
print(ordencao_por_selecao(arr))
