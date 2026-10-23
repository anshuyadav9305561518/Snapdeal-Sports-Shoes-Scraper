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
