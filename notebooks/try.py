import pandas as pd 

df = pd.read_csv("./data/raw/train.csv")
#print(len(df[(df['Gender'] == "Male") & (df['Vehicle_Damage'] == "Yes")]))
#print(df.isnull().sum())
print(df)
#print(pd.get_dummies(df, drop_first= 1))
#df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes': "Tut Gya", 'No': "Bach Gya"})

# print(len(df[
#     (df['Gender']=="Male")
#     &
#     (df['Age'].duplicated())
# #['Age'].unique()
# &
# (df['Response'] ==1)]))

print(df.describe())