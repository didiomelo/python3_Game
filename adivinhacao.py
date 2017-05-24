import random

def play() :
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = [0, 20, 10, 5]
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    for rodada in range(1, total_de_tentativas[nivel] +1) :

        print("Tentativa {} de {}".format(rodada, total_de_tentativas[nivel]))

        chute_str = input("Digite um numero entre 1 e 100:")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        if(chute < 1 or chute > 100) :
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")

    print("Fim do jogo")

if(__name__ == "__main__") :
    play()
