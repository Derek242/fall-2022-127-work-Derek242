#Extra: 
# 1)Handle upper and lower case and/or punctuation
# 2)

pirate = open('pirate.dat','r')
speech = open('input.txt','r')
pirate_speech = pirate.read()
sentences = speech.read().lower()
pirate2 = pirate_speech.split()
speech2 = speech.split('\n')

i = 0
story =[]
dictionary = {}
for i in speech2:
    semi = word.find(':')
    dict.update({word[0:semi]:word[semi+1:]})

for i in pirate2:
    if word in dictionary.keys():
        story.append(dictionary[i])
    else:
        story.append(word)
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