#Jogo feito por mim vini PEDRA, PAPEL OU TESOURA
import random

def jogo():
    while True:

        bot = random.choice(["PEDRA", "PAPEL", "TESOURA"])
        entrada = input("Digite 'PEDRA', 'PAPEL' ou 'TESOURA': ").upper()

        while (entrada not in["PEDRA", "PAPEL", "TESOURA"]):
            print("ERRO! As opções são --> 'PEDRA', 'PAPEL' ou 'TESOURA'")
            entrada = input("Digite 'PEDRA', 'PAPEL' ou 'TESOURA': ").upper()

        print("Sua Escolha: {}".format(entrada))
        print("Escolha do Bot: {}".format(bot))

        if (entrada == bot):
            print("Empate!!!")
        elif (entrada == "TESOURA" and bot == "PAPEL") or (entrada == "PEDRA" and bot == "TESOURA") or (entrada == "PAPEL" and bot == "PEDRA"):
            print("Você Ganhou!!!")
        else:
            print("Você Perdeu!!!")

        op = input("Informe [J] para jogar novamente, ou [S] para sair: ").upper()
        while (op not in ["J", "S"]):
            print("ERRO! As opções são --> [J] ou [S]")
            op = input("ERRO! Digite [J] para jogar novamente, ou [S] para sair: ").upper()

        if op == "S":
            break

jogo()