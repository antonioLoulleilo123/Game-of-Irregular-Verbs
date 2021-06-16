import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
####


import random
import pygame
import time

pygame.init()

#Sounds
lose = pygame.mixer.Sound("data/sounds/lose.mp3")
win = pygame.mixer.Sound("data/sounds/Winsound.wav")

PastVerb = 0
Continuar = ''
Present = 0
cont = 0
counter = 0
num = ['']
Past = 0
B = ('be', 'become', 'begin', 'blow', 'break', 'bring', 'build', 'buy')
C = ('can', 'catch', 'choose', 'come', 'cut')
D = ('do', 'drink', 'drive')
E = 'eat'
F = ('fight', 'find', 'fly', 'forget')
G = ('get', 'give', 'go')
H = 'have'
K = ('keep', 'know')
L = ('learn', 'leave', 'lose')
M = ('make', 'meet')
P = ('pay', 'put')
R = ('read', 'ride', 'run')
S = ('say', 'see', 'send', 'shine', 'sing', 'sleep', 'speak', 'spend', 'swim')
T = ('take', 'teach', 'think', 'throw')
U = 'understand'
W = ('wake', 'win', 'write')

Bpast = ('was', 'became', 'began', 'blew', 'broke', 'brought', 'built', 'bought')
Cpast = ('could', 'caught', 'chose', 'came', 'cut')
Dpast = ('did', 'drank', 'drove')
Epast = 'ate'
Fpast = ('fought', 'found', 'flew', 'forgot')
Gpast = ('got', 'gave', 'went')
Hpast = 'had'
Kpast = ('kept', 'knew')
Lpast = ('learnt', 'left', 'lost')
Mpast = ('made', 'met')
Ppast = ('paid', 'put')
Rpast = ('read', 'rode', 'ran')
Spast = ('said', 'saw', 'sent', 'shone', 'sang', 'slept', 'spoke', 'spent', 'swam')
Tpast = ('took', 'taught', 'thought', 'threw')
Upast = 'understood'
Wpast = ('woke', 'won', 'wrote')

print('WARNING, to stop this "game" you have to write "stop" <-- just like this ')

while True:

    PastSimple = random.randint(1, 17)
    counter += 1
    num[0] = 0
    num.append(PastSimple)

    if PastSimple == num[cont-1]:
        PastSimple = random.randint(1, 17)
        num[counter] = PastSimple

    if PastSimple == 1:
        Verbs = random.randint(0, 7)
        if Verbs == 0:
            Present = B[0]
            PastVerb = Bpast[0]
        if Verbs == 1:
            Present = 'become'
            PastVerb = 'became'
        if Verbs == 2:
            Present = B[2]
            PastVerb = Bpast[2]
        if Verbs == 3:
            Present = B[3]
            PastVerb = Bpast[3]
        if Verbs == 4:
            Present = B[4]
            PastVerb = Bpast[4]
        if Verbs == 5:
            Present = B[5]
            PastVerb = Bpast[5]
        if Verbs == 6:
            Present = B[6]
            PastVerb = Bpast[6]
        if Verbs == 7:
            Present = B[7]
            PastVerb = Bpast[7]
    elif PastSimple == 2:
        Verbs = random.randint(0, 4)
        if Verbs == 0:
            Present = C[0]
            PastVerb = Cpast[0]
        if Verbs == 1:
            Present = C[1]
            PastVerb = Cpast[1]
        if Verbs == 2:
            Present = C[2]
            PastVerb = Cpast[2]
        if Verbs == 3:
            Present = C[3]
            PastVerb = Cpast[3]
        if Verbs == 4:
            Present = C[4]
            PastVerb = Cpast[4]
    elif PastSimple == 3:
        Verbs = random.randint(0, 2)
        if Verbs == 0:
            Present = D[0]
            PastVerb = Dpast[0]
        if Verbs == 1:
            Present = 'drink'
            PastVerb = 'drank'
        if Verbs == 2:
            Present = 'drive'
            PastVerb = 'drove'
    elif PastSimple == 4:
        Verbs = 0
        if Verbs == 0:
            Present = E
            PastVerb = Epast
    elif PastSimple == 5:
        Verbs = random.randint(0, 3)
        if Verbs == 0:
            Present = F[0]
            PastVerb = Fpast[0]
        if Verbs == 1:
            Present = F[1]
            PastVerb = Fpast[1]
        if Verbs == 2:
            Present = F[2]
            PastVerb = Fpast[2]
        if Verbs == 3:
            Present = F[3]
            PastVerb = Fpast[3]
    elif PastSimple == 6:  # letra G
        Verbs = random.randint(0, 2)
        if Verbs == 0:
            Present = G[0]  # get
            PastVerb = Gpast[0]
        if Verbs == 1:
            Present = G[1]  # give
            PastVerb = Gpast[1]
        if Verbs == 2:
            Present = 'go'  # go
            PastVerb = 'went'
    elif PastSimple == 7:
        Verbs = 0
        if Verbs == 0:
            Present = 'have'  # have
            PastVerb = 'had'
    elif PastSimple == 8:
        Verbs = random.randint(0, 1)
        if Verbs == 0:
            Present = 'keep'  # keep
            PastVerb = 'kept'
        if Verbs == 1:
            Present = K[1]  # know
            PastVerb = Kpast[1]
    elif PastSimple == 9:
        Verbs = random.randint(0, 2)
        if Verbs == 0:
            Present = L[0]
            PastVerb = Lpast[0]
        if Verbs == 2:
            Present = L[2]
            PastVerb = Lpast[2]
        if Verbs == 3:
            Present = L[3]
            PastVerb = Lpast[3]
    elif PastSimple == 10:
        Verbs = random.randint(0, 1)
        if Verbs == 0:
            Present = M[0]
            PastVerb = Mpast[0]
        if Verbs == 1:
            Present = 'meet'
            PastVerb = 'met'
    elif PastSimple == 11:
        Verbs = random.randint(0, 1)
        if Verbs == 0:
            Present = P[0]
            PastVerb = Ppast[0]
        if Verbs == 1:
            Present = 'put'
            PastVerb = 'put'
    elif PastSimple == 12:
        Verbs = random.randint(0, 8)
        if Verbs == 0:
            Present = R[0]
            PastVerb = Rpast[0]
        if Verbs == 1:
            Present = R[1]
            PastVerb = Rpast[1]
        if Verbs == 2:
            Present = R[2]
            PastVerb = Rpast[2]
    elif PastSimple == 13:
        Verbs = random.randint(0, 8)
        if Verbs == 0:
            Present = S[0]
            PastVerb = Spast[0]
        if Verbs == 1:
            Present = S[1]
            PastVerb = Spast[1]
        if Verbs == 2:
            Present = S[2]
            PastVerb = Spast[2]
        if Verbs == 3:
            Present = S[3]
            PastVerb = Spast[3]
        if Verbs == 4:
            Present = S[4]
            PastVerb = Spast[4]
        if Verbs == 5:
            Present = S[5]
            PastVerb = Spast[5]
        if Verbs == 6:
            Present = S[6]
            PastVerb = Spast[6]
        if Verbs == 7:
            Present = S[7]
            PastVerb = Spast[7]
        if Verbs == 8:
            Present = S[8]
            PastVerb = Spast[8]
    elif PastSimple == 14:
        Verbs = random.randint(0, 8)
        if Verbs == 0:
            Present = T[0]
            PastVerb = Tpast[0]
        if Verbs == 1:
            Present = T[1]
            PastVerb = Tpast[1]
        if Verbs == 2:
            Present = T[2]
            PastVerb = Tpast[2]
        if Verbs == 3:
            Present = T[3]
            PastVerb = Tpast[3]
    elif PastSimple == 15:
        Verbs = 0
        if Verbs == 0:
            Present = U
            PastVerb = Upast
    elif PastSimple == 16:
        Verbs = random.randint(0, 2)
        if Verbs == 0:
            Present = W[0]
            PastVerb = Wpast[0]
        if Verbs == 1:
            Present = 'win'
            PastVerb = 'won'
        if Verbs == 2:
            Present = W[2]
            PastVerb = Wpast[2]

    Past = str(input(f'What is the Past Simple of {Present}?'))

    if Past == PastVerb:
        print('Congratulations, You answered right!')
        win.play()
        cont += 1
    elif Past == 'stop':
        print('Bye, See you later')
        break
    else:
        print(f'You are wrong, the correct answer is {PastVerb}')
        if cont == 0:
            print("You have to study more didn't hit any")
        elif cont <= 4:
            print(f"You have to study more, you only answer {cont} questions right")
        else:
            print(f"Congratulations, you got {cont} questions right")
        lose.play()
        time.sleep(5)
        break
