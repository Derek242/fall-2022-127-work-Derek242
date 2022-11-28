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
    dict.update({i[0:semi]:i[semi+1:]})

def dictionary(dict):
    story = []
    i=0
    for k in pirate2:
        if k in dict.keys():
            story.append(dict[i])
        else:
            story.append(i)
        if story[k] == story[0]:
            story[k] = story[k].capitalize()
        elif "." in story[k-1]:
            story[k] = story[k].captialize()
        elif "!" in story[k-1]:
            story[k] = story[k].captialize()
        elif "?" in story[k-1]:
            story[k] = story[k].captialize()
        elif ";" in story[k-1]:
            story[k] = story[k].captialize()
    i += 1
    return ' '.join(story)
    
print("Pirate Speech: " + dictionary(dict_pirate))