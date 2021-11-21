#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%%
data = pd.read_csv('Data/lending_club_loan_dataset.csv')
data.head()

print('Total number of rows -> ' + str(data.shape[0]))
print('Total number of variables -> ' + str(data.shape[1]))

#%%