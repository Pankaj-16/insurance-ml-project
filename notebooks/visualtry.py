import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns
df = pd.read_csv('./data/raw/train.csv')

# sns.histplot(df['Age'], kde=True, bins=20)
# mp.title('Age Distribute')
# mp.xlabel('Age')
# mp.ylabel('Count')
# mp.show()

# sns.boxplot(x='Gender', y='Annual_Premium', data=df)
# mp.title('Smoker Charge')
# mp.show()

# sns.countplot(x='Age',kde=True, data=df)
# mp.title('Age count')
# mp.show()

mp.figure(figsize=(10,6))
selected_cols = ['Age', 'Region_Code','Response']
sns.heatmap(df[selected_cols].corr(), annot=True, cmap= 'coolwarm')
mp.title('Matrix')
mp.show()