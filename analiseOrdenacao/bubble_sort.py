import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def gerar_lista_aleatoria(tamanho):
    return [random.randint(1, 10000000) for _ in range(tamanho)]

def rodar_testes():
    tamanhos = [10, 100, 1000, 5000, 10000, 50000, 100000]

    print("--- Testando Bubble Sort ---")
    for tamanho in tamanhos:
        dados = gerar_lista_aleatoria(tamanho)
        start_time = time.perf_counter()
        bubble_sort(dados)
        end_time = time.perf_counter()
        tempo_execucao = end_time - start_time
        print(f"  Tamanho {tamanho}: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    rodar_testes()
