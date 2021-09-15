#Jogo da forca.

import getpass

print('Ola! Este é o jogo da forca, onda uma pessoa digita a PALAVRA SECRETA\n e outra tenta advinhar qual é a palavra, digitando apenas uma latra.')

palavra_secreta = getpass.getpass('Digite a palavra secreta: ')
digitadas = []
chances = 3

print (f'A a palavra secreta tem {len(palavra_secreta)} letras.')

while True:
    if chances <= 0:
        print('\n Fim de Jogo!')
        break
    
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('\n Só pode digitar apenas uma letra')
        chances -= 1
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'\n Eba! A letra {letra}, existe na palavra secreta!')
    else:
        print(f'\n A letra digitada não existe na palavra secreta.')
        digitadas.pop()

    palavra_temp = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitadas:
            palavra_temp += letra_secreta
        else:
            palavra_temp += '*'

    if palavra_temp == palavra_secreta:
        print(f'\n Aeee!! A palavra secreta é {palavra_secreta}! \n')
        break
    else:
        print(f'\n Quase lá, a palavra secreta ainda está assim: {palavra_temp} \n')    

    if letra not in palavra_secreta:
        chances -= 1
    print(f'\n Você ainda tem {chances} chances. \n')

