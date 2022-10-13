# Write a function to find the smallest value in a listKfind smallest in a list of items
l = [4,7,10,5]

def smallest(listKfind):
  small = listKfind[0]
  for i in (listKfind):
    if i < small:
      small = i
  return small
  
print(smallest(l))

#Write a function that returns a new list that contains all the odd items in the original list
l = [1,5,17,20,567,28,60]
def odd(l):
  oddlist = []
  for i in l:
    if i%2 == 1:
      oddlist.append(i)
  return oddlist

print(odd(l))
  
#Write a function that takes a string and returns a new string where all the words are capitalized.
lower = ["derek ni"]
upper = []
def caplist(word):
  nl = ''
  for i in word.split():
        upper += i.captalize() + " " # CAPITALIZE EACH WORD AND ADD IT TO NEWLIST
   return upper
  

  
#Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case

def more_than_five(l):
    finalList = []
    for i in l.split():
        if len(i) > 4: 
            i = i.upper()
        newlist.append(i)
        sentence = " ".join(newlist)
    return sentence
  
#Write a function that takes a list of numbers and returns a new list with each item squared
lis = [2,3,4,5]
def squareRoot(l):
  squaredList = []
  for i in l:
    i = i**2
    squaredList.append(i)
  return squaredList
print(squareRoot(lis))
  
#Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
lis1 = [1,2,3,4,5]
lis2 = [6,7,8,9,10]
def combineList(l1,l2):
  counter = 0
  finalList = []
  for i in lis1:
      finalList.append(i+l2[counter])
      counter = counter + 1
  return finalList

print(combineList(lis1,lis2))
#chapter 10:
#10
lis = ["Banana","Monke", "Billy"]
def fiveletters(l):
  finalList = []
  for i in l:
    if len(i) >= 5:
      finalList.append(i)
  return finalList
print(fiveletters(lis))

#11
lis = [1,3,7,9,5,2]
def sum_of_odds(l):
  finalList = []
 for i in l:
   if num%2 == 0:
     return finalList
   else:
    finalList = finalList + i

print(sum_of_odds(lis))

#12
def count_sam(l):
  counter = 0
for i in l:
  counter = counter + 1
  if i == "sam":
    return l

