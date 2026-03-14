import random

pontos = 0

print("-" * 60)
print("Corrida do Mario")
print("=" * 60)

print("Ajude o Mario a chegar ao castelo com a maior pontuação")

while True:
    print("=" * 60)
    print(f"PONTUAÇÃO ATUAL: {pontos}")
    print("O que Mario irá fazer?")
    print("1 - Pular")
    print("2 - Pegar moeda")
    print("3 - Atacar inimigo")
    print("4 - Sair")
    print("-" * 60)
    
    try:
        acao = int(input("Digite o número da ação (1 a 4): "))
        if acao == 1:
            if random.choice([True, False]):
                print(">Yahoo! Você pulou um buraco perfeitamente! (+10 pontos)")
                pontos += 10
            else:
                print(" Oops! Você tropeçou em uma raiz ao pular(-5 pontos)")
                pontos -= 5
                
        elif acao == 2:
            if random.choice([True, False]):
                print("Yuppi! Mario conseguiu pegar a moeda dourada!(+20 pontos)")
                pontos += 20
            else:
                print(" Ai! O tijolo era duro demais para Mario222222(-20 pontos)")
                pontos -= 20
            
        elif acao == 3:
            if random.choice([True, False]):
                print(" Bumba! Você pulou em cima de um Goomba e o derrotou! (+50 pontos)")
                pontos += 50
            else:
                print(" Ai! O inimigo foi mais rápido e você tomou um chega pra lá(-20 pontos)")
                pontos -= 20
                
        elif acao == 4:
            print("\n" + "=" * 60)
            print("Chegada no Castelo!")
            print(f"Sua pontuação final foi de: {pontos} pontos")
            print("=" * 60)
            break
        else:
            print(" Ação inválida! Por favor, escolha um número de 1 a 4")
            
    except ValueError:
        print(" Erro: Entrada inválida, digite apenas o números da opção")