pontos = 0

print("1. Qual é o resultado da expressão `2 ** 3` em Python?")
print("A) 6")
print("B) 8")
print("C) 9")
resposta = input("Sua resposta: ")
if resposta == "B" or resposta == "b":
    pontos = pontos + 1

print("2. Qual das seguintes estruturas de dados é considerada 'mutável' em Python?")
print("A) Tupla (tuple)")
print("B) String")
print("C) Lista (list)")
resposta = input("Sua resposta: ")
if resposta == "C" or resposta == "c":
    pontos = pontos + 1

print("3. Qual é a sintaxe correta para iniciar a definição de uma função?")
print("A) def minha_funcao():")
print("B) function minha_funcao():")
print("C) create minha_funcao():")
resposta = input("Sua resposta: ")
if resposta == "A" or resposta == "a":
    pontos = pontos + 1

print("4. Qual palavra-chave é utilizada com o bloco `try` para tratamento de exceções?")
print("A) catch")
print("B) error")
print("C) except")
resposta = input("Sua resposta: ")
if resposta == "C" or resposta == "c":
    pontos = pontos + 1

print("5. Qual é o principal objetivo da função embutida `len()`?")
print("A) Encontrar o maior número em uma lista.")
print("B) Retornar a quantidade de itens (comprimento) de um objeto.")
print("C) Converter uma string para minúsculas.")
resposta = input("Sua resposta: ")
if resposta == "B" or resposta == "b":
    pontos = pontos + 1

print("\n--- Resultado ---")
print("Pontuação:", pontos)

if pontos <= 2:
    print("Nível: Aprendiz")
elif pontos <= 4:
    print("Nível: Programador Intermediário")
else:
    print("Nível: Mestre Python")