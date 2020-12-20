# Importação da biblioteca necessária
from math import log, factorial

# Inicialização do vetor de 10 posições
vetor= [0]*10

# Loop para atribuição de valores
for i in range (len(vetor)):
  if i%2 == 0:
    vetor[i] = pow(3,i)+7*(factorial(i))
  else:
    vetor[i] = pow(2,i) + 4*log(i)

# Obtenção dos valores médio e máximo
vetor_max = max(vetor)
vetor_media = sum(vetor)/len(vetor)

# Exibição dos resultados
print("Vetor final:", vetor)
print("Maior valor contindo no vetor: ", vetor_max)
print("Média dos valores: ", round(vetor_media,2))