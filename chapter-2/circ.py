#2.8
#Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

radius = input("What is the radius?")

radius = int(radius)
pi = 3.141592653589
area = (radius**2) * pi

print(pi)
print(area)

print("The area of the circle would be: " + str(area))
