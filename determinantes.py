from random import randint

def calc_menor(matriz: list[list[int]], i_entrada: int, j_entrada: int) -> list[list[int]]:
    menor_ij = []
    for lin in range(len(matriz)):
        # se estiver na linha da entrada, nós pulamos
        if i_entrada == lin:
            continue
        linha = []
        for col in range(len(matriz)):
            # se estiver na coluna da entrada, nós pulamos
            if j_entrada == col:
                continue
            linha.append(matriz[lin][col])
        menor_ij.append(linha)

    return menor_ij

def calc_cofator(matriz: list[list[int]], i_entrada: int, j_entrada: int) -> int:
    menor_ij = calc_menor(matriz, i_entrada, j_entrada)
    cofator_ij = (-1) ** (i_entrada + j_entrada) * calc_determinante(menor_ij)
    return cofator_ij

def calc_determinante(matriz: list[list[int]]) -> int:
    # o determinante de uma matriz 1x1 é igual a sua única entrada
    if len(matriz) == 1:
        return matriz[0][0]
    
    # pode assumir qualquer valor tal que 0 <= COLUNA_ESCOLHIDA < N
    COLUNA_ESCOLHIDA = randint(0, len(matriz) - 1)

    # LINHA_ESCOLHIDA = randint(0, len(matriz) - 1)
    # pode-se calcular o determinante por linha, desde que, da mesma forma
    # 0 <= LINHA_ESCOLHIDA < N

    determinante = 0
    for indice in range(len(matriz)):
        determinante += matriz[indice][COLUNA_ESCOLHIDA] * calc_cofator(matriz, indice, COLUNA_ESCOLHIDA)

        # caso esteja calculando por linha
        # determinante += matriz[LINHA_ESCOLHIDA][indice] * calc_cofator(matriz, LINHA_ESCOLHIDA, indice)


    return determinante

def main():
    N = int(input()) # tamanho da matriz (quadrada)

    matriz: list[list[int]] = []
    for _ in range(N):
        linha = [int(i) for i in input().split()]
        matriz.append(linha)
    
    det = calc_determinante(matriz)
    print(det)

if __name__ == '__main__': 
    main()