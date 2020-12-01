from palavras import carro, animal, cor
import random
import numeros

# Verificação

def verifica_acerto(palavra, tentativa, acertos):
    acertou = False
    for x in palavra:
        if tentativa == x:
            acertou = True
            acertos.append(x)
            return acertou
    return acertou
        

def verificar_tentativa(acertos):
    for x in acertos:
            break

#Mostrar acertos

def mostrar_acertos(palavra, acerto):
    if acertos == []:
        print(len(palavra) * '_')
        return
    exibe = ''
    for x in palavra:
        existe = False
        for y in acerto:
            if x == y:
                exibe = exibe + y
                existe = True
                break
        if existe == False:
            exibe = exibe + '_'
    print(exibe)
    
# Status do jogo

def exibir_forca(tentativas):
  estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  print(estagios[tentativas])


# Saudações

jogador1 = input("Digite o seu nome ")

multisingle = int(input("Bem vindo,%s! Escolha o seu modo de jogo. 1/2 (1 - Singleplayer, 2 - Multiplayer) " % jogador1))

if multisingle == 1:
    print("Vamos começar!")

if multisingle == 2:
    jogador2 = input("Digite o nome do segundo jogador ")
    print("Bem-vindo, %s! Vamos começar!" % jogador2)

#Jogo

i = int(input("Escolha a opçao!\n 1-carro\n 2-animal\n 3-cor\n "))

if i == 1:
    vetor = carro
elif i == 2:
    vetor = animal
elif i == 3:
    vetor = cor

palavra = format(random.choice(vetor))
palavra2 = format(random.choice(vetor))

#Tentativas jogador1

i = -1

x = 6

acertos = []
repetidas = []

while i <= len(palavra):
    exibir_forca(x)
    mostrar_acertos(palavra,acertos)
    print(palavra)
    print(" ")
    tentativa = input("Escolha uma letra ")
    tentativa = tentativa.lower()
    if tentativa == palavra:
        print("A palavra é " + tentativa)
        print("Parabéns, você acertou!")
        print("Obrigado por jogar! Jogue novamente quantos vezes quiser.")
        break
    if verifica_acerto(palavra, tentativa, acertos):
        if tentativa in repetidas:
            print("Não escolha uma letra repetida")
        else:
            repetidas.append(tentativa)
            print("Parabéns, %s , você acertou uma letra!" % jogador1)
    else:
        print("Puts, %s, você errou =(" % jogador1)
        x -= 1
        i += 1

# Tentativas jogador 2

if multisingle == 2:
    print("Agora é a vez de %s" % jogador2)
    while i <= len(palavra2):
        exibir_forca(x)
        mostrar_acertos(palavra2, acertos)
        print(palavra2)
        print(" ")
        tentativa = input("Escolha uma letra ")
        tentativa = tentativa.lower()
        if tentativa == palavra2:
            print("A palavra é " + tentativa)
            print("Parabéns, você acertou!")
            print("Obrigado por jogar! Jogue novamente quantos vezes quiser.")
            break
        if verifica_acerto(palavra2, tentativa, acertos):
            if tentativa in repetidas:
                print("Não escolha uma letra repetida")
            else:
                repetidas.append(tentativa)
                print("Parabéns, %s , você acertou uma letra!" % jogador1)
        else:
            print("Puts, %s, você errou =(" % jogador1)
            x -= 1
            i += 1from palavras import carro, animal, cor
import random
import numeros

# Verificação

def verifica_acerto(palavra, tentativa, acertos):
    acertou = False
    for x in palavra:
        if tentativa == x:
            acertou = True
            acertos.append(x)
            return acertou
    return acertou
        

def verificar_tentativa(acertos):
    for x in acertos:
            break

#Mostrar acertos

def mostrar_acertos(palavra, acerto):
    if acertos == []:
        print(len(palavra) * '_')
        return
    exibe = ''
    for x in palavra:
        existe = False
        for y in acerto:
            if x == y:
                exibe = exibe + y
                existe = True
                break
        if existe == False:
            exibe = exibe + '_'
    print(exibe)
    
# Status do jogo (Função e homem na forca retirado de matheusbattisti)

def exibir_forca(tentativas):
  estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]

  print(estagios[tentativas])


# Saudações

jogador1 = input("Digite o seu nome ")

multisingle = int(input("Bem vindo,%s! Escolha o seu modo de jogo. 1/2 (1 - Singleplayer, 2 - Multiplayer) " % jogador1))

if multisingle == 1:
    print("Vamos começar!")

if multisingle == 2:
    jogador2 = input("Digite o nome do segundo jogador ")
    print("Bem-vindo, %s! Vamos começar!" % jogador2)

#Jogo

i = int(input("Escolha a opçao!\n 1-carro\n 2-animal\n 3-cor\n "))

if i == 1:
    vetor = carro
elif i == 2:
    vetor = animal
elif i == 3:
    vetor = cor

palavra = format(random.choice(vetor))
palavra2 = format(random.choice(vetor))

#Tentativas jogador1

i = -1

x = 6

acertos = []
repetidas = []

while i <= len(palavra):
    exibir_forca(x)
    mostrar_acertos(palavra,acertos)
    print(" ")
    tentativa = input("Escolha uma letra ")
    tentativa = tentativa.lower()
    if tentativa == palavra:
        print("A palavra é " + tentativa)
        print("Parabéns, você acertou!")
        print("Obrigado por jogar! Jogue novamente quantos vezes quiser.")
        break
    if verifica_acerto(palavra, tentativa, acertos):
        if tentativa in repetidas:
            print("Não escolha uma letra repetida")
        else:
            repetidas.append(tentativa)
            print("Parabéns, %s , você acertou uma letra!" % jogador1)
    else:
        print("Puts, %s, você errou =(" % jogador1)
        x -= 1
        i += 1

# Tentativas jogador 2

if multisingle == 2:
    print("Agora é a vez de %s" % jogador2)
    while i <= len(palavra2):
        exibir_forca(x)
        mostrar_acertos(palavra2, acertos)
        print(" ")
        tentativa = input("Escolha uma letra ")
        tentativa = tentativa.lower()
        if tentativa == palavra2:
            print("A palavra é " + tentativa)
            print("Parabéns, você acertou!")
            print("Obrigado por jogar! Jogue novamente quantos vezes quiser.")
            break
        if verifica_acerto(palavra2, tentativa, acertos):
            if tentativa in repetidas:
                print("Não escolha uma letra repetida")
            else:
                repetidas.append(tentativa)
                print("Parabéns, %s , você acertou uma letra!" % jogador1)
        else:
            print("Puts, %s, você errou =(" % jogador1)
            x -= 1
            i += 1