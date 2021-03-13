from random import randint as rnd
import numpy as np

code = ['a', 'b', 'c', 'd',
        'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p',
        'q', 'r', 's', 't',
        'u', 'v', 'w', 'x',
        'y', 'z', ',', '.',
        '!', '?', ' ', '\n']

def ChooseRandProb(arr):
    which = rnd(0, 10000)/100
    summ = sum(arr)
    if(summ == 0):
        return(rnd(0, len(arr)))
    where = 0
    for i in range(len(code)):
        where += arr[i]*100.0/summ
        if where >= which:
            return(i)
    if(i >= len(code)):
        return(len(code)-1)
    return(len(code)-1)

def ReadText(text):
    text = text.lower()
    probs = np.zeros((32, 32, 32, 32))
    for i in range(0, len(text)-3):
        x = code.index(text[i])
        y = code.index(text[i+1])
        z = code.index(text[i+2])
        a = code.index(text[i+3])
        probs[x, y, z, a] += 1
    return(probs)

def Generate(start, probs):
    outText = start.lower()
    for i in range(2, 100):
        x = code.index(outText[i])
        y = code.index(outText[i-1])
        z = code.index(outText[i-2])
        what = ChooseRandProb(probs[x, y, z])
        print(what)
        if(what >= 32):
            what = 31
        outText += code[what]
    return(outText)

print(Generate('Hello', ReadText(open("data.txt", "r").read())))