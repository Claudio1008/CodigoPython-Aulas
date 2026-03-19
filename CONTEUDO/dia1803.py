'''frutas = []
frutas.append("laranja")
frutas.append("maçã")
frutas.append("manga")
frutas.append("banana")
frutas.sort()
frutas.insert(0,"orange")
frutas.append("uva")
frutas.clear()

print(frutas)'''


'''numeros = []
for i in range(8):
    valor = int(input("DIGITE UM NUMERO: "))
    numeros.append(valor)
    numeros.sort()
    print("numeros digitados: ", numeros)'''

# somar todos os numeros do array

'''soma = []
for i in range(10):
    valor = int(input("DIGITE UM NUMERO: "))
    soma.append(valor)
    resultado = sum(soma)
    print(f"a soma de todos os nuemros é: {resultado}")'''


# exeercici 03 - media e classificação , leia 6 notas e informe: media da turma, quantoa ficaram acima da media e quantos ficaram abaixo da media


'''notas = []
for i in range(6):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

acima_media = 0
abaixo_media = 0

for nota in notas:
    if nota > media:
        acima_media += 1
    elif nota < media:
        abaixo_media += 1

print(f"Notas da turma: {notas}")
print(f"Média da turma: {media:.2f}")
print(f"Alunos acima da média: {acima_media}")
print(f"Alunos abaixo da média: {abaixo_media}")

# modo mais facil 
notas = []
soma = 0
for i in range(6):
    nota = float(input("digite a nota: "))
    notas.append(nota)
    soma += nota
    media = soma / 6
    aima = 0
    abaixo = 0
for n in notas:
    if n >= media:
        acima += 1
    else:
        abaixo += 1'''



'''numeros = []
for i in range(6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

maior_valor = max(numeros)
menor_valor = min(numeros)

posicao_maior = numeros.index(maior_valor)
posicao_menor = numeros.index(menor_valor)

print(f"Lista completa: {numeros}")
print(f"O MAIOR valor é {maior_valor} e está na posição {posicao_maior}.")
print(f"O MENOR valor é {menor_valor} e está na posição {posicao_menor}.")'''



temperaturas = []
for i in range(10):
    temp = int(input(f"DIGITE A TEMPERATURA DO DIA {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / len(temperaturas)

acima_media = 0
for t in temperaturas:
    if t > media:
        acima_media += 1

maiorTemp = max(temperaturas)
menorTemp = min(temperaturas)

print(f"TEMPERATURAS: {temperaturas}")
print(f"A MÉDIA FOI: {media:.1f} GRAUS") 
print(f"MAIOR: {maiorTemp}° | MENOR: {menorTemp}°")
print(f"DIAS ACIMA DA MÉDIA: {acima_media}")