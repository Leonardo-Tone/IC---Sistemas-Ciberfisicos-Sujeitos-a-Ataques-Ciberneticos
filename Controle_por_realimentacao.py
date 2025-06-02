from Functions import *
from scipy.signal import place_poles
import numpy as np

def main():
    print("=== Sistema de Controle por Realimentação de Estados ===")
    print("Matriz A:")
    A = criar_matriz()
    print("Matriz B:")
    B = criar_matriz()

    print("\nVerificando controlabilidade...")
    if not verificar_controlabilidade(A, B):
        print("O sistema não é controlável. Não é possível projetar o controlador por realimentação de estados.")
        return

    print("\nVerificando estabilidade da matriz A...")
    verificar_estabilidade(A)

    print("\nDigite os autovalores desejados para o sistema em malha fechada (um por linha, pressione Enter para finalizar):")
    autovalores_desejados = []
    while True:
        val = input("Autovalor (ou Enter para terminar): ").strip()
        if val == "":
            break
        try:
            autovalores_desejados.append(complex(val))
        except ValueError:
            print("Valor inválido. Tente novamente.")

    if len(autovalores_desejados) != len(A):
        print("A quantidade de autovalores deve ser igual à ordem da matriz A.")
        return

    # Cálculo do ganho de realimentação de estados (K)
    try:
        A_np = np.array(A)
        B_np = np.array(B)
        resultado = place_poles(A_np, B_np, autovalores_desejados)
        K = resultado.gain_matrix
        print("\nMatriz de ganho K calculada para os autovalores desejados:")
        print(K)
    except ImportError:
        print("A biblioteca scipy é necessária para o cálculo do ganho K (função place_poles). Instale usando 'pip install scipy'.")
    except Exception as e:
        print("Erro ao calcular o ganho K:", e)

if __name__ == "__main__":
    main()

