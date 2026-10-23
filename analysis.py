import pandas as pd

# Load dataset
df = pd.read_csv("data/sports_shoes.csv")

print("Dataset loaded successfully!")
print(df.head())

# Brand list
brands = [
    "Campus",
    "Clymb",
    "Vector X",
    "ASIAN",
    "Aivin",
    "OFF LIMITS",
    "Bersache",
    "JQR",
    "Avant",
    "RODOX",
    "Spartan",
    "PENNEN",
    "JK Port",
    "hotstyle"
]

# Function to identify brand
def find_brand(product_name):

    for brand in brands:
        if brand.lower() in product_name.lower():
            return brand

    return "Other"


# Create Brand column
df["Brand"] = df["Product_Name"].apply(find_brand)

print("\nBrand-wise data:")
print(df[["Product_Name", "Brand"]].head(20))


# Top brands
top_brands = df["Brand"].value_counts()

print("\nTop Brands:")
print(top_brands)



print("\nPrice Analysis:")

print("Average Selling Price:",
      round(df["Selling_Price"].mean(), 2))

print("Minimum Selling Price:",
      df["Selling_Price"].min())

print("Maximum Selling Price:",
      df["Selling_Price"].max())

print("Average Discount:",
      round(df["Discount_Percentage"].mean(), 2))



# Highest discount products
highest_discount = df.sort_values(
    by="Discount_Percentage",
    ascending=False
).head(5)

print("\nTop 5 Highest Discount Products:")
print(highest_discount[
    [
        "Product_Name",
        "Selling_Price",
        "Original_Price",
        "Discount_Percentage"
    ]
])


# Best rated products
best_rated = df.sort_values(
    by="Rating",
    ascending=False
).head(5)

print("\nTop 5 Rated Products:")
print(best_rated[
    [
        "Product_Name",
        "Rating",
        "Reviews"
    ]
])


# Most reviewed products
most_reviewed = df.sort_values(
    by="Reviews",
    ascending=False
).head(5)

print("\nTop 5 Most Reviewed Products:")
print(most_reviewed[
    [
        "Product_Name",
        "Reviews",
        "Rating"
    ]
])


import matplotlib.pyplot as plt

# -------------------------------
# 1. Top Brands Chart
# -------------------------------

top_brands = df["Brand"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_brands.plot(kind="bar")

plt.title("Top 10 Brands by Number of Products")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/top_brands.png")
plt.show()


# -------------------------------
# 2. Price Distribution
# -------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    df["Selling_Price"],
    bins=10
)

plt.title("Distribution of Selling Prices")
plt.xlabel("Selling Price (₹)")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("charts/price_distribution.png")
plt.show()


# -------------------------------
# 3. Discount Distribution
# -------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    df["Discount_Percentage"],
    bins=10
)

plt.title("Distribution of Discount Percentage")
plt.xlabel("Discount (%)")
plt.ylabel("Number of Products")

plt.tight_layout()
plt.savefig("charts/discount_distribution.png")
plt.show()


# Final cleaned dataset
df.to_csv(
    "data/final_sports_shoes.csv",
    index=False
)

print("\nFinal dataset saved successfully!")
print("File: data/final_sports_shoes.csv")



print("\nFinal Dataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


Haan, meri galti thi. 👍 `README.md` me jo content diya tha, usme formatting ki wajah se confusion ho gaya. **Tum `README.md` ko ab completely clean karke ye exact content paste karo.**

### 1. Pehle `README.md` ka pura purana content delete karo

**Ctrl + A → Delete**

### 2. Phir ye exact content paste karo:

# Snapdeal Men's Sports Shoes Web Scraping & Analysis

## Project Overview

This project is a Python-based web scraping and data analysis project.

The project collects men's sports shoes data from Snapdeal and analyzes product prices, discounts, ratings, reviews, and brands.

## Objective

The main objectives of this project are:

* Scrape men's sports shoes product data from Snapdeal.
* Collect product names and pricing information.
* Extract discount percentages.
* Extract product ratings and review counts.
* Identify product brands.
* Store the collected data in CSV format.
* Perform basic data analysis.
* Create visualizations to understand the collected data.

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* Matplotlib

## Data Collected

The following information is collected for each product:

* Product Name
* Brand
* Selling Price
* Original Price
* Discount Percentage
* Rating
* Number of Reviews

## Project Structure

```text
Snapdeal_Sports_Shoes_Scraper/
│
├── charts/
│   ├── top_brands.png
│   ├── price_distribution.png
│   └── discount_distribution.png
│
├── data/
│   ├── sports_shoes.csv
│   └── final_sports_shoes.csv
│
├── scraper.py
├── analysis.py
├── requirements.txt
└── README.md
```

## Web Scraping

The `scraper.py` file uses:

* Requests to send an HTTP request to Snapdeal.
* BeautifulSoup to parse the HTML page.
* Pandas to create and save the dataset.

The scraper collected 20 men's sports shoes products.

## Data Analysis

The `analysis.py` file performs analysis on the collected dataset.

The analysis includes:

### Brand Analysis

Campus has the highest number of products in the collected dataset with 4 products.

Vector X has 3 products.

Clymb and Aivin have 2 products each.

### Price Analysis

* Average Selling Price: ₹816.30
* Minimum Selling Price: ₹310
* Maximum Selling Price: ₹1,364

### Discount Analysis

* Average Discount: 63.8%
* Highest Discount: 84%

### Rating Analysis

The highest observed product rating is 4.5 out of 5.

### Review Analysis

The most reviewed product in the collected dataset has 4,231 reviews.

## Visualizations

The project includes the following visualizations:

1. Top 10 brands by number of products
2. Selling price distribution
3. Discount percentage distribution

The charts are stored inside the `charts` folder.

## Dataset

The collected data is stored in CSV format.

The final dataset contains the following columns:

* Product_Name
* Selling_Price
* Original_Price
* Discount_Percentage
* Rating
* Reviews
* Brand

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
```

### Step 2: Run the Scraper

```bash
python scraper.py
```

This will collect the product data and create:

```text
data/sports_shoes.csv
```

### Step 3: Run the Analysis

```bash
python analysis.py
```

This will perform the analysis and generate the visualizations.

## Conclusion

This project demonstrates how Python can be used for web scraping, data cleaning, data analysis, and visualization.

The project provides insights into men's sports shoes available on Snapdeal, including product prices, discounts, brands, ratings, and customer reviews.
