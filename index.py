import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('file.csv',sep=';')
sns.scatterplot(df, x='x',y='y',hue='c')
plt.show()