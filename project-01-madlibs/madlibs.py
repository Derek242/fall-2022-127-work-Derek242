#Importing random
import random

#opens files and returning them in variables

verbs = open("verbs.dat")
nouns = open("nouns.dat")
hero = open("hero.dat")
lines = open("lines.dat")
adj = open("adjective.dat")
adv = open('adverb.dat')

#reads the files
verbsR = verbs.read()
nounsR = nouns.read()
heroR = hero.read()
linesR = lines.read()
adjR = adj.read()
advR = adv.read()

#seperating every word into a string
verbL = verbsR.split()
nounsL = nounsL.split()
heroL = heroR.split()
adjL = adjR.split()
advL = advR.split()

def madlibs():
  #splitting the line and creating a variable for the new story
  linesL = lines.split()
  newL = ''
  hero_name = random.choice(heroL)
  for l in linesL:
    if l == "<NOUN>":
      newL += (" "+random.choice(nounsL))
    elif l == "<VERB>":
      newL += (" "+random.choice(verbL))
    elif l == "<HERO>":
      newL += (" "+hero_name)
    elif l == "<ADJECTIVE>":
      newL += (" "+random.choice(adjL))    
    elif l == "<ADVERB>":
      newL += (" "+random.choice(advL))  
  print(newL)

madlibs()