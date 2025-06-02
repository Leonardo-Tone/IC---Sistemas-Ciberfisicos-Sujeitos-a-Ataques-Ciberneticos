import numpy as np
import random

def criar_matriz():
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))
    escolha = input("Deseja inserir os valores manualmente (M) ou gerar aleatoriamente (A)? ").strip().upper()

    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if escolha == 'M':
                valor = float(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            else:
                valor = random.randint(-5, 10)
            linha.append(valor)
        matriz.append(linha)
    return matriz

def verificar_controlabilidade(A, B):
    """ 
    Verifica se o sistema (A, B) é controlável.
    A e B devem ser listas de listas (matrizes).
    """
    A = np.array(A)
    B = np.array(B)
    n = A.shape[0]
    # Construção da matriz de controlabilidade
    controlabilidade = B
    for i in range(1, n):
        controlabilidade = np.hstack((controlabilidade, np.linalg.matrix_power(A, i) @ B))
    posto = np.linalg.matrix_rank(controlabilidade)
    print("Matriz de controlabilidade:\n", controlabilidade)
    print("Posto da matriz de controlabilidade:", posto)
    if posto == n:
        print("O sistema é controlável.")
        return True
    else:
        print("O sistema NÃO é controlável.")
        return False

def verificar_estabilidade(A):
    """
    Verifica se o sistema representado pela matriz A é estável.
    Retorna True se todos os autovalores têm parte real negativa.
    """
    A = np.array(A)
    autovalores = np.linalg.eigvals(A)
    print("Autovalores da matriz A:", autovalores)
    if np.all(np.real(autovalores) < 0):
        print("O sistema é estável (todos os autovalores têm parte real negativa).")
        return True
    else:
        print("O sistema NÃO é estável (existe autovalor com parte real não-negativa).")
        return False

