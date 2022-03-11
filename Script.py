#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.axisgrid import pairplot
#%%
data = pd.read_csv('Data/lending_club_loan_dataset.csv')
data.head()
#%%
print('Total number of rows -> ' + str(data.shape[0]))
print('Total number of variables -> ' + str(data.shape[1]))
# %%
data.describe().T.round(3)
# %%
data.describe(include= np.object).T
# %%
null_values = pd.DataFrame(data.isna().sum())
null_values['Null proportion'] = null_values/len(data)*100
null_values

# %%
null_values['Null proportion'].plot(kind = 'bar', color = 'red')

# %%
data['bad_loan'].value_counts().plot(kind = 'pie',
 subplots = True,autopct='%1.2f%%')
# We can see thath we are working with a very unbalaced dataset
# %%
data.dtypes
# %%
data.hist(figsize=(15,10), color = 'red')
# %%
sns.pairplot(data)
# %%
for col in data.select_dtypes(include = ['object']).columns:
    data[col].value_counts().plot(kind = 'bar',
    color = sns.color_palette('mako'))
    plt.title(col)
    plt.show()

    
# %%
data['last_major_derog_none'].fillna(0, inplace = True)
data.isna().sum()
# %%
sns.boxplot(x = 'bad_loan', y = 'annual_inc', data = data)
print('Total number of households with anual income above 500k: ' + 
str(sum(data['annual_inc'] >= 500000)))
# %%
sns.boxplot(x = 'bad_loan', y = 'emp_length_num', data = data)
# %%
sns.catplot(x = 'grade',data = data, hue = 'bad_loan',
 kind = 'count', palette = 'Paired')
plt.grid()
# %%
sns.catplot(x = 'home_ownership',data = data, hue = 'bad_loan',
 kind = 'count', palette = 'Paired')
plt.grid()
# %%

data['term'] = data['term'].str.replace('36 Months', '36 months')
for col in data.select_dtypes(include = ['object']).columns:
    sns.catplot(x = col ,data = data, hue = 'bad_loan',
    kind = 'count', palette = 'Paired')
    plt.grid()
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.show()
# %%
