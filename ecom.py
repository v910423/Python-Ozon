import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('ecom.csv', encoding='unicode_escape')

print(df.shape)
print(df.head())
print(df.columns)