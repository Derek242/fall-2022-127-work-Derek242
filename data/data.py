#3 Extras: 2 more analysis on dataset and a bar graph for first cereal brands
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

def cereal_ratings():
    number_of_cereal = 0
    total_rating = 0
    for i in cereal_stuff["rating"]:
      total_rating = total_rating + i
      number_of_cereal+=1
    print("The average rating of all Cereal is: " , (total_rating)/(number_of_cereal))

cereal_sugar()
cereal_cals()
cereal_ratings()

#Chart for calorie data
all_cereal_names = cereal_stuff["name"]
first_five_names = all_cereal_names.head()
all_cereal_cals = cereal_stuff["calories"]
first_five_cals = all_cereal_cals.head()

def bars():
  size = plot.figure(figsize = (10,5))
  plot.bar((first_five_names),(first_five_cals),color = 'orange',width = 1)
  plot.xlabel("Cereal Brands")
  plot.ylabel("Amount of Calories")
  plot.title("Cereals")
  plot.show()

bars()