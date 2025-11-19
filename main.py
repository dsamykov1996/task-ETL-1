import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 180)

url = "https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv"

df_origin = pd.read_csv(url)

COLUMNS_TO_DROP = []

print("\n--- head ---")
print(df_origin.head())
print("\n--- info ---")
print(df_origin.info())
print("\n--- describe ---")
print(df_origin.describe)

print("\n--- describe for str ---")
print(df_origin.describe(include=[object]).T)

print("--- null ---")
# print(df.isna().sum())
print(df_origin.isna().sum().sort_values(ascending=False).head(20))

print("--- duplicates ---")
print(df_origin.duplicated().sum())

print("--- List columns ---")
list_col = df_origin.columns
print(list(list_col))
for i, col in enumerate(df_origin.columns):
    print(f"{i:02d}. {col}")


# 2. Cleaning datas

df = df_origin.copy()

if COLUMNS_TO_DROP:
    print("\n--- delete columns inlist ---")
    df_origin = df.drop(columns=[col for col in COLUMNS_TO_DROP if col in df.columns], errors="ignore")


# columns = []    
    # for col in COLUMNS_TO_DROP:
    #     if col in df_raw.columns:
    #         columns.append(col) (die code von 46 bis 49 linie ist GLEICH WIE IN 43 LINIE)

else:
    print("\nCOLUMNS_TO_DROP = []")

def standardize_text(s):
    if pd.isna(s):
        return np.nan
    
    if not isinstance(s, str):
        s = str(s)

    s = s.strip()
    s = " ".join(s.split())

    return s     

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].apply(standardize_text)


# print(df)

possible_email_cols = [c for c in df.columns if "email" in c.lower()]
possible_web_cols = [c for c in df.columns if ("web" in c.lower() or "website" in c.lower() or "url" in c.lower())]
possible_phone_cols = [c for c in df.columns if ("phone" in c.lower() or "telephone" in c.lower() or "tel" in c.lower())]
possible_fax_cols = [c for c in df.columns if "fax" in c.lower()]

# list generation
# [variable(with operations) for variable in where we are looking for]
# [0, 1, 2, 3]
# [n for n in range(4)]

print("\nPossible columns:")
print("Email:", possible_email_cols)
print("Web cols:", possible_web_cols)
print("Phone cols:", possible_phone_cols)
print("Fax cols:", possible_fax_cols)


# aplling variables

for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].apply(standardize_text)

# email
for col in possible_email_cols:
    df[col] = df[col].str.lower()   

# web
for col in possible_web_cols:
    df[col] = df[col].str.lower() 




