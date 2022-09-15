#7.7: Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(n):
  if (n % 2 == 0):
    return True
  else:
    return False
print(is_even(5))
print(is_even(8))

#7.8: Now write the function is_odd(n) that returns True when n is odd and False otherwise.

def is_odd(n):
  if (n % 2 == 1):
    return True
  else:
    return False
print(is_odd(5))
print(is_odd(8))

#7.10-11: Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

#Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as


def is_rightangled(x,y,z):
  xa = x**2
  ya = y**2
  za = z**2
  if(xa+ya==za or ya+za==xa or xa+za==ya):
    #Extend the above program so that the sides can be given to the function in any order.
    return True
  else:
    return False
print(is_rightangled(3,4,5))
print(is_rightangled(4,8,10))

########### Coding Bat: String #1 ####################
#helloName 
def hello_name(name):
  return "Hello " + name +"!"

  
#makeOutWord
def make_out_word(out, word):
  return out[0:2] + word + out[2:4]


#firstTwo
def first_two(str):
 return str[0:2] 
