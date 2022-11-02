
list = [20,19,15,200,58,82,22,69]

def findLargest(l):
  smallest = list[0]
  for i in l:
    if i > smallest:
      smallest = i
    return smallest

print(findLargest(list))


value = 69
lis = [9,69,5,19,1,5,25,69,48]

def freq(l,v):
  count = 0
  for i in l:
    if i == v:
      count += 1
  return count

print(freq(lis,value))


import random
def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive
    def buildRandomList(size,maxvalue):
      #result = []
     #for x in range(size):
      #    result.append(random.randrange(maxvalue))
      #return result
     result = [random.randrange(maxvalue) for x in range(size)]
     return result 


    # 1. make a list of 100 slots
    # and set them all to 0
    # this will store our tallies
    newL = []
    tallies = 0
    

    # 2. Loop through our dataset
    # and for each item incremement
    # (add 1) to the appropriate
    # slot in the tallies list

    # 3. the index with the highest
    # value in tallies is the mode

    pass
