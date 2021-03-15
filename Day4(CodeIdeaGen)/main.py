from random import randint as rnd

def Load():
    content = open('data.txt').read().splitlines()
    dir = {}
    key = ''
    for stroke in content:
        if(len(stroke) > 1):
            if(stroke[0] == '~'):
                command = stroke[1:]
                if(command == 'end'):
                    key = ''
                else:
                    key = stroke[1:]
                    dir[stroke[1:]] = []
                continue
            dir[key].append(stroke)
    return(dir)

def Check(text, dir):
    reading = False
    word = ''
    for i in range(len(text)):
        if text[i] == '[':
            reading = True
            continue
        elif text[i] == ']':
            reading = False
            key = '[' + word + ']'
            text = text.replace(key, dir[word][rnd(0, len(dir[word])-1)])
            break
        if reading: word += text[i]
    return(text)
        


def Generate():
    dir = Load()
    idea = dir['template'][rnd(0, len(dir['template'])-1)]
    for i in range(10): idea = Check(idea, dir)
    print(idea)
Generate()