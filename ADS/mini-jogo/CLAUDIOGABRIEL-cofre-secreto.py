codigoCofre = 4221
tentativas = 1

while True:
    try:
        senha = int(input("Digite a senha do cofre em numeros (ex:0000): "))
        if codigoCofre == senha:
            print("Senha CORRETA! Cofre aberto")
            break
        else:
            print("Senha ERRADA! Acesso Negado")
            print("tente Novamente")
            print(f"TENTATIVAS = {tentativas}")
            tentativas += 1

    except ValueError:
        print("resposta invalida! digite somente numeros")