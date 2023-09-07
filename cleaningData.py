import pandas as pd
import numpy as np


df = pd.read_csv('D:\DEBeginner\Project2\car\car.csv')


df = df[['name','price','origin','status','KMtraveled','color','doorNumber','engine','fuelConsumption']]
df.to_csv('car/car.csv', sep='\t', encoding='utf-8')