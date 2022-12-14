#Extras: One more analysis on dataset and a bar graph for the ratio (sugar:calories)
# import stuff
import random
import pandas as pd
import matplotlib.pyplot as plot
import csv

#brinigng the data into the code
cereal = open('cereal.csv')
cereal_stuff = pd.read_csv(cereal)
print(cereal_stuff.to_string())

#Finding average amount of calories and sugar from all brands of cereal from given data
def cereal_cals():
    number_of_cereal = 0
    total_cals = 0
    for i in cereal_stuff["calories"]:
      total_cals = total_cals + i
      number_of_cereal+=1
    print("The average amount of calories in Cereal is: " , (total_cals)/(number_of_cereal))


def cereal_sugar():
    number_of_cereal = 0
    total_sugars = 0
    for i in cereal_stuff["sugars"]:
      total_sugars = total_sugars + i
      number_of_cereal+=1
    print("The average amount of sugar in Cereal is: " , (total_sugars)/(number_of_cereal))

cereal_sugar()
cereal_cals()

#Chart for calorie data

all_cereal_cals = cereal_stuff["calories"]
all_cereal_sugars = cereal_stuff["sugars"]
first_five_cals = all_cereal_cals.head
first_five_sugars = all_cereal_sugars.head

def fatass(cals):
    
    plot.bar()

    return 