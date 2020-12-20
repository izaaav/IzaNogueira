# Definição da quantidade de alunos e inicialização do dicionário
qtd_alunos = 5
dic = {}

# Loop para coleta de dados do usuário
for i in range(qtd_alunos):
  nome = input('Qual o nome do aluno? ')
  nota = input('Qual a nota do aluno? ')
  dic[nome] = float(nota)
  
# Exibição do resultado
print(dic)
print("A maior nota foi: ")
print(max(dic.items(), key = lambda x: x[1]))
