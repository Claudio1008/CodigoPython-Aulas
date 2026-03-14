import random

numeroSecreto = random.randint(1, 50)
tentativaAtual = 1
maxTentativas = 5

print("O Tesouro Perdido da Ilha Python")
print(f"Cuidado: você tem {maxTentativas} pás para cavar!")

while tentativaAtual <= maxTentativas:
    try:
        print(f"Tentativa {tentativaAtual} de {maxTentativas}")
        encontrandoTesouro = int(input("Escave um número de 1 a 50: "))

        if encontrandoTesouro == numeroSecreto:
            print("Boa escavada, você acertou!")
            break
        else:
            if encontrandoTesouro < numeroSecreto:
                print("Dica: O tesouro está em um número MAIOR.")
            else:
                print("Dica: O tesouro está em um número MENOR.")

            tentativaAtual += 1

    except ValueError:
        print("Isso não é número! Você perdeu o foco e uma tentativa.")
        tentativaAtual += 1

    finally:
        print("Finalizando Escavações!")

if tentativaAtual > maxTentativas:
    print(f"Suas pás quebraram, O número correto era {numeroSecreto}. Tente novamente em outra ilha")
