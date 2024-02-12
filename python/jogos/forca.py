import random

def apresentacao():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
def busca_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    return palavras[random.randrange(0, len(palavras))].upper()

def formata_campo_palavra_secreta(palavra_secreta):
    return ["_" for _ in palavra_secreta]

def captura_chute():
    return input("Qual letra? ").strip().upper()

def verifica_chute(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("       _______________        ")
    print("      /               \       ")
    print("     /                 \      ")
    print("   //                   \/\   ")
    print("   \|   XXXX     XXXX   | /   ")
    print("    |   XXXX     XXXX   |/    ")
    print("    |   XXX       XXX   |     ")
    print("    |                   |     ")
    print("    \__      XXX      __/     ")
    print("      |\     XXX     /|       ")
    print("      | |           | |       ")
    print("      | I I I I I I I |       ")
    print("      |  I I I I I I  |       ")
    print("      \_             _/       ")
    print("        \_         _/         ")
    print("          \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def jogar():
    apresentacao()

    enforcou = False
    acertou = False
    erros = 0

    palavra_secreta = busca_palavra_secreta()
    letras_acertadas = formata_campo_palavra_secreta(palavra_secreta)

    while(not enforcou and not acertou):
        chute = captura_chute()

        if(chute in palavra_secreta):
            verifica_chute(palavra_secreta, letras_acertadas, chute)
        else:
            erros += 1

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    print("------------------------------")
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

if(__name__ == "__main__"):
    jogar()
