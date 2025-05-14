# notebooks/01_data_exploration.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set some aesthetics for seaborn
sns.set(style="whitegrid")

# Load the dataset (replace with your actual file path)
df = pd.read_csv("./data/train.csv")

# Basic info
print("Shape of dataset:", df.shape)
print("\nColumn info:\n")
print(df.info())

# First few rows
print("\nSample data:\n")
print(df.head())

# Summary stats
print("\nStatistical Summary:\n")
print(df.describe(include='all'))

# Missing values
print("\nMissing values:\n")
print(df.isnull().sum())
