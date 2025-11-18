import pandas as pd
import numpy as np

url = "https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv"

df = pd.read_csv(url)
df.head()
df.info()
df.describe()

df.isna().sum()
df.duplicated().sum()

df["email"] = df["email"].str.lower()
df["web"] = df["web"].str.lower()



df["phone1"] = df["phone1"].str.replace("-", "")
df["phone2"] = df["phone2"].str.replace("-", "")
df["phone1"] = df["phone1"].str.strip()
df["phone2"] = df["phone2"].str.strip()

print(df)









