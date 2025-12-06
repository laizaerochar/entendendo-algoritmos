# exercício 1.1: Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?
# exercício 1.2: Suponha que você duplique o tamanho da lista do exercício 1.1 (256 nomes agora). Qual seria o número máximo de etapas agora?


import math

def busca_binaria(tamanho_lista):
    if tamanho_lista <= 0:
        return 0

    max_etapas = math.ceil(math.log2(tamanho_lista))
    return int(max_etapas)


n = input("Digite a quantidade de elementos na sua lista:")
n_int = int(n)
max_n_etapas = busca_binaria(n_int)
print(f"Para um lista com {n_int} elementos, o número máximo de etapas da busca binária é {max_n_etapas} etapas.")

    
