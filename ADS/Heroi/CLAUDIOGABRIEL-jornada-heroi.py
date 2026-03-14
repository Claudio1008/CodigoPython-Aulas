import random

vidas = 3

print("Bem-vindo a Jornada do Heroi!")
print("Voce precisa atravessar a floresta e sobreviver a 3 desafios.")

print("Voce encontrou uma caverna.")
print("1 - Entrar")
print("2 - Continuar pela floresta")
escolha = input("O que voce faz? ")

if escolha == '1':
    print("Voce achou um atalho seguro.")
else:
    print("Voce tropecou em espinhos e perdeu vida.")
    vidas -= 1

if vidas > 0:
    print("Um guardiao pergunta: Quanto e 7 x 8?")
    print("1 - 54")
    print("2 - 56")
    escolha = input("Sua resposta: ")
    
    if escolha == '2':
        print("Resposta correta. Pode passar!")
    else:
        print("Resposta errada. O guardiao te atacou e voce perdeu vida.")
        vidas -= 1

if vidas > 0:
    print("Voce ouve um barulho suspeito nos arbustos.")
    print("1 - Investigar")
    print("2 - Fugir")
    escolha = input("O que voce faz? ")
    
    if escolha == '1':
        evento = random.choice(["monstro", "tesouro"])
        if evento == "tesouro":
            print("Sorte grande! Voce encontrou uma pocao.")
        else:
            print("E um monstro! Voce perdeu vida.")
            vidas -= 1
    else:
        print("Voce correu e escapou.")

if vidas > 0:
    print("VITORIA! Voce sobreviveu e salvou o reino!")
else:
    print("DERROTA! Suas vidas acabaram.")