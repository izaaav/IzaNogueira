# Inicialização do contador para o total de números que cumprem as condições
numeros = 0

# Loop para verificação das condições
for i in range(1, 5000000):
  if (i%2 == 0) and (i%49 == 0) and (i%37 == 0):
    numeros += 1

# Exibição dos resultados  
print("Existem "+str(numeros)+" valores que satisfazem as condfições.")