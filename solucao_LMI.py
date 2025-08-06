from Functions import *
import numpy as np
import cvxpy as cp

#Criando a matriz A
A = np.array([[0, 1], [0, 0]])
#A = np.array([[0, 1], [-1, 2]])
#A = np.array([[0, 1], [-2, -3]])
#A = np.array([[-0.3937, 0.4057], [0.1763, -0.1964]])
#A = np.array(criar_matriz())

#Varificando o posto da matriz A
n = A.shape[0]

#Definindo a variável de otimização P
P = cp.Variable((n, n), PSD=True)

#Definindo as restrições do problema de otimização (condição de Lyapunov: A^T * P + P * A < 0)
restrições = [A.T @ P + P @ A << 0]

#Definindo o custo do problema de otimização
custo = cp.trace(P)
objetivo = cp.Minimize(custo)

#Definindo o problema de otimização 
problema = cp.Problem(objetivo, restrições)

#Resolvendo o problema de otimização
problema.solve(verbose= False)
if problema.status == "optimal":
    problema_status = "Problema resolvido com sucesso."
else:  
    problema_status = "O problema não foi resolvido com sucesso."
#Exibindo os resultados
print("=== Resolução do Problema de Otimização LMI ===")
print("Matriz A:", A)
print("Matriz P:", P.value)
print("Autovalores de P:", np.linalg.eig(P.value)[0])
print(problema_status)
print(problema.status)