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

# clean phone/fax
def clean_phone(x):
    if pd.isna(x):
        return np.nan
    s = str(x)
    s = s.strip()


    # plus = ""
    # if s.startswith("+"):
    #     plus = "+"
    
    plus = "+" if s.startswith("+") else ""

    # digits = ""
    # for ch in s:
    #     if ch.isdigit():
    #         digits += ch

    digits = "".join(ch for ch in s if ch.isdigit())  

    if digits == "":
        return np.nan      
    return plus + digits
        

for col in possible_phone_cols + possible_fax_cols:
    df[col] = df[col].apply(clean_phone)

def title_if_str(s):
    if pd.isna(s):
        return np.nan
    return str(s).title()

city_cols = [c for c in df.columns if "email" in c.lower() in ("city", "city_name", "town")]

address_cols = [c for c in df.columns if "email" in c.lower() in ("address")]

name_cols = [c for c in df.columns if c.lower() in ("name", "first_name", "second_name", "company_name", "last_name")] 

name_title = city_cols + address_cols + name_cols

if name_title:
    for c in name_title:
        df[col] = df[col].apply(title_if_str)
    print("n\--- name of title ---")
else:
    print("n\--- haven't name ---")        


#3. Creating new columns (Feature Engineering)

df["full_name"] = df.first_name + df.last_name

df["email_domain"] = df["email"].str.split("@").str[-1]

df["city_lenght"] = df["city"].apply(len)

df["is_gmail"] = [True if "@gmail.com" in str(s).lower() else False for s in df["email"]]

# print([bool(s) for s in df["email"] if "@gmail.com" in str(s).lower()])

#4 Filtring datas

print("\n--- підвибірки ---")

gmail_users = df.loc[df["is_gmail"] == True].copy()
print(gmail_users)

print("Gmail users:", len(gmail_users))

# workers companies of "LLC" or "LTD"

# df["company_name"]
df["company_name"] = df["company_name"].fillna("")

mask_LLC_Ltd = df.company_name.str.contains(r"\b(LLC|Ltd|llc|LTD|ltd)\b", regex=True, na=False)
# print(mask_LLC_Ltd)

company_llc_ltd = df.loc[mask_LLC_Ltd].copy()
# print(company_llc_ltd)

print("Company LLC and Ltd:", len(company_llc_ltd))

#5 позиційна вибірка

try:
    first_10_cols_2_5 = df.iloc[:10, 2:6]
    print("\nFirst 10 cols and 2-5 str")
    print(first_10_cols_2_5)
except Exception as e:
    print("can't first 10 str + colmns 2-5:", e)



every_10th = df.iloc[::10, :].copy()
print("\nevery_10th")
print(every_10th)    

random_5th = df.sample(5, random_state=42)
print("\nrandom_5th_row")
print(random_5th)

#6. Grouping and statistic




# print(df.head())    



