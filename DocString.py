import pandas as pd

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Create a dataframe from a dict
import pandas as pd
from numpy.random import randint

df = pd.DataFrame(columns=['lib', 'qty1', 'qty2'])
for i in range(5):
    df.loc[i] = ['name' + str(i)] + list(randint(10, size=2))

print(df)