import random
import time
import datetime
import pickle
import re



def init_scramble(): #Returns a list of 10 randomly generated alphabets
    scrambled_alphs = [] # WARNING : Scrambles all previous data
    for i in range(10):
        characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890)(*&^%$#@!~`-=_+][{}\\|:;/.,<>?")
        alph = []
        for i in range(len(characters)):
            char = random.choice(characters)
            alph.append(char)
            characters.remove(char)
        scrambled_alphs.append(''.join(alph))
    pickle.dump(scrambled_alphs, open('alphs.p', 'wb'))


def ebets(alph_num): #Used in key in pull alphabet
    alphs = pickle.load(open('alphs.p', 'rb'))
    return alphs[alph_num]


def e_1(key, inp): # Syntax : e_1('111', 'encrypt me') <-- key has to be in string format
    key = list(map(int, str(key)))
    inp = re.sub(' ', '_', inp)
    bird_word = []
    final_word = []
    alph = ebets(key[0])
    for i in inp:
        index = alph.index(i)
        if index == 91:
            i = alph[0 + key[1]]
        if index == 91:
            i = alph[0 + (key[1] - 1)]
        else:
            i = alph[index + key[1]]
        bird_word.append(i)
    bird_word = ''.join(bird_word)
    for i in range(10):
        fake_word = []
        for ii in range(random.randint(2, (len(inp) + random.randint(0, len(inp))))):
            fake_word.append(random.choice(alph))
        if key[2] == i:
            final_word.append(bird_word)
        else:
            final_word.append(''.join(fake_word))
    return ' '.join(final_word)



def d_1(key, inp):
    key = list(map(int, str(key)))
    inp = inp.split()
    bird_word = []
    alph = ebets(key[0])
    for i in inp[key[2]]:
        index = alph.index(i)
        if index == 0:
            i = alph[91 - key[1]]
        if index == 1:
            i = alph[91 - (key[1] + 1)]
        else:
            i = alph[index - key[1]]
        bird_word.append(i)
    return ''.join(bird_word)
        
