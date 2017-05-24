import forca
import adivinhacao

def escolhe_seu_jogo():
    print("*********************************")
    print("******** ESCOLHA SEU JOGO *******")
    print("*********************************")

    print("(1) FORCA (2) ADIVINHACAO")
    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando forca...")
        forca.play()
    elif(jogo == 2):
        print("Jogando adivinhacao...")
        adivinhacao.play()

if(__name__ == "__main__"):
    escolhe_seu_jogo()
