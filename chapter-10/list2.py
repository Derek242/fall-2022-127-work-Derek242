#Chapter 10.4

numlist = [10,9,14,17]

def average(numlist):
  total = 0
  for num in numlist:
    total = total + num
  return total / len(numlist)

print(average(numlist))

#Chapter 10.6
nums = [2,3,4]
def sum_of_squares(xs):
  sum = 0
  for i in xs: 
    sum = sum + (i**2)
  return sum

print(sum_of_squares(nums))
  