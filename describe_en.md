# 📘 Project Summary

## ✔ What Was Done
Throughout the data analysis and cleaning process, the following steps were completed:

1. Loaded the raw dataset and performed an initial overview:
   - `head()`, `info()`, `describe()`
   - checked missing values and duplicates
   - reviewed column list and structure

2. Data cleaning:
   - removed extra spaces and standardized text
   - converted email addresses to lowercase
   - cleaned phone numbers (kept only digits and optional "+")
   - normalized the casing of names, cities and addresses

3. Feature engineering:
   - created `full_name` by combining first and last name
   - extracted `email_domain` from each email
   - added `city_length` — the length of the city name
   - added `is_gmail` — a binary Gmail indicator

4. Data filtering and sampling:
   - created a subset of Gmail users
   - filtered companies with “LLC” or “LTD”
   - positional selections using `iloc`
   - random sampling using `sample`

5. Grouping and statistics:
   - number of people per city
   - number of unique email domains per city
   - TOP-5 cities
   - TOP-5 email domains
   - aggregated statistics using `groupby()` and `agg()`

6. Export of results:
   - `cleaned.csv` — cleaned dataset
   - `gmail_users.csv` — filtered Gmail users
   - `tops.xlsx` — Excel file with two sheets (top cities and domains)

---

## ⚠ Problems Found in the Dataset
During data inspection, the following issues were identified:

- inconsistent text formatting (mixed case, extra spaces)
- unstandardized email formats
- phone numbers containing non-numeric characters
- a few missing values
- some potential duplicates
- inconsistent naming of cities and companies

---

## ⭐ Most Useful Transformations
- Text standardization → improved grouping and matching  
- Phone number cleaning → unified formatting  
- Extracting `email_domain` → enabled domain analysis  
- Adding `is_gmail` → quick segmentation of Gmail users  
- Aggregation with `agg()` → multiple metrics in a single step  

---

## 🔍 Interesting Findings and Insights
- Gmail is the most popular email provider in the dataset.
- A small number of cities contain most of the records (TOP-5).
- “LLC” and “LTD” companies cluster in certain cities.
- City name lengths look consistent — no anomalies.
- Email domain segmentation is strong and useful for marketing.

---

## 🚀 Future Improvements
1. Use `phonenumbers` library for advanced phone validation.
2. Normalize city names using a mapping dictionary.
3. Add geolocation data and build geographic visualizations.
4. Perform deeper analysis of email domain patterns.
5. Implement anomaly detection for unusual entries.
6. Turn the entire workflow into an automated data-processing pipeline.