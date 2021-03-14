from gtts import gTTS
from playsound import playsound


def menu():
    resposta = input('(S) Seguir\n'
                     '(N) Sair\n')
    return resposta

y = menu()

while y != 'N'.lower():

    def play():
        x = input('Texto: ')
        voz = gTTS(x, lang='pt')
        voz.save('x.mp3')
        playsound('x.mp3')

    play()

    menu()

else:
    exit()

