#Extra: 
# 1)Handle upper and lower case and/or punctuation


pirate = open('pirate.dat')
speech = open('input.txt')
pirate_speech = pirate.read()
sentences = speech.read().lower()
pirate2 = pirate_speech.split('\n')
speech2 = speech.split('\n')

i = 0
story =[]
dictionary = {}
for i in speech2:
    semi = i.find(':')
    dict.update({i[0:semi]:i[semi+1:]})

for i in pirate2:
    if i in dictionary.keys():
        story.append(dictionary[i])
    else:
        story.append(i)
    if story[i] == story[0]:
        story[i] = story[i].capitalize()
    elif "." in story[i-1]:
        story[i] = story[i].captialize()
    elif "!" in story[i-1]:
        story[i] = story[i].captialize()
    elif "?" in story[i-1]:
        story[i] = story[i].captialize()
    elif ";" in story[i-1]:
        story[i] = story[i].captialize()
    i+= 1
    
print(' '.join(story))