import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def gerar_lista_aleatoria(tamanho):
    return [random.randint(1, 10000000) for _ in range(tamanho)]

def rodar_testes():
    tamanhos = [10, 100, 1000, 5000, 10000, 50000, 100000]

    print("--- Testando Insertion Sort ---")
    for tamanho in tamanhos:
        dados = gerar_lista_aleatoria(tamanho)
        start_time = time.perf_counter()
        insertion_sort(dados)
        end_time = time.perf_counter()
        tempo_execucao = end_time - start_time
        print(f"  Tamanho {tamanho}: {tempo_execucao:.6f} segundos")

if __name__ == "__main__":
    rodar_testes()
