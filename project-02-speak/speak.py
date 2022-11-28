#Extra: 
# 1)Handle upper and lower case and/or punctuation

speech = open('input.txt')
pirate = open('pirate.dat')
pirate_speech = pirate.read()
sentences = speech.read().lower()
pirate2 = pirate_speech.split()
speech2 = sentences.split()


dict_pirate = {}
for i in speech2:
    semi = i.find(':')
    dict_pirate.update({i[0:semi]:i[semi+1:]})

def dictionary(dict):
    story = []
    i=0
    for i in pirate2:
        if i in dict.keys():
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
    return ' '.join(story)
    
print("Pirate Speech: " + dictionary(dict_pirate))