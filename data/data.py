import random
import pandas as pd
import matplotlib.pyplot as plot
import csv

cereal = open('cereal.csv')
cereal_stuff = pd.read_csv(cereal)
print(cereal_stuff.to_string())
