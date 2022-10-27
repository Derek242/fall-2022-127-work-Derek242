
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
    if x == v:
      count += 1
  return count

print(freq(lis,value))


modeSoFar = dataset[0]
freqSoFar = freq(dataset,modeSoFar)
for item in dataset[1:]:
  modeSoFar = item
  freqSoFar = freq(dataset, item)
return modeSoFar

def testMode(size, maxV):
  dataset = builtRandom(size, maxV)
  print(dataset)
  m = mode(dataset)
  print(m)
  