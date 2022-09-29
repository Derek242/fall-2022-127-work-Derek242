def bondify(name):
    result = ""
    first = name[0]
    first = first.upper()
    result = result + first + "."
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result
  
print(bondify("Derek Ni"))
print(bondify("derek ni"))

#piglatin

def piglatin(word):
    first = word[0].lower()
    length = len(word)
    p = word[length-1]
    if(first in 'aeiou'):
      if(word[length-1] in '.,?!'):
        word = word[0:length - 1] + 'yay' + p
        return word.capitalize()
    else:
      word = word[1:length-1] + word[0].lower() + 'ay' + p
      return word.capitalize()

print(piglatin('Piglatin!'))
print(piglatin('Firefighter.'))
print(piglatin("Hello?"))
print(piglatin("amen"))
