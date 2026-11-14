# Conteúdo 02 - Estruturas Condicionais (if, elif e else)
# .if (se), o elif (senão se) e o else (senão).

# para o que serve?
# Fazer o programa tomar decisões com base em certas condições.

# 1. A Estrutura Básica (if e else)
# O if testa se uma condição é verdadeira
# (True). Se for, ele executa o bloco de código dentro dele.
# Se não for, ele pula para o else.

idade = 18

if idade >= 18:
    print("você é maior de idade, Você pode tirar CNH")
else:
    print("você é menor de idade.")

# 2. Lidando com Várias Condições (elif)
# E se você precisar testar mais de duas opções?
# Usamos o elif (uma abreviação de else if).
# O Python vai testar as condições em ordem de
# cima para baixo; assim que uma for verdadeira,
# ele executa e encerra o bloco.

nota = 5
if nota >= 9:
    print("nota A: Aprovado. ganha Premio.")
elif nota >= 7:
    print("nota B: Aprovado.")
elif nota >= 5:
    print("nota C: recuperação")
else:
    print("nota D: reprovado")

# Outro exemplo só que ultilizando média
nota_1 = 5.0
nota_2 = 3.0
media = (nota_1 + nota_2)/2
print(f"\nSua média é: {media}")


if media >= 6.0:
    print("Situação: Aprovado! ")
elif media >= 5.0:
    print("Situação: Recuperação. ")
else:
    print("Situação: Reprovado. ")
