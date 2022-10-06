# Exercise 10.5
def max(nums):
    max = 0
    for e in nums:
        if e > max:
            max = e
    return max

nums = [1,4,8,11]
print(max(nums))

# Exercise 10.7

def countOdd(nums):
    odd = 0
    for i in nums: 
        if i % 2 !=0:
            odd = odd + 1
    return odd

oddNum = str(countOdd(nums))
print("There are " + oddNum + " odd numbers.")

import random 

nums = []
for i in range(100):
    numlib.append(random.randint(0, 1000))

print(nums)

#Exercise 10.8
import random 

def sumEven(evens):
    sum = 0 
    for i in evens:
        if i > 0:
            sum = sum + i 
    return sum 

print(sumEven(evens))

evens = []
for i in range(100): 
    evenlib.append(random.randrange(-100, 100))

print(sumEven(evens))


