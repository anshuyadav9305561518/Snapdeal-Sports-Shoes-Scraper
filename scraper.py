import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://www.snapdeal.com/products/men-sports-footwear"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.select(".product-tuple-listing")

print("Number of products found:", len(products))

data = []

for product in products:

    # Product Name
    name = product.select_one(".product-title")

    # Selling Price
    price = product.select_one(".product-price")

    # Original Price
    original_price = product.select_one(".product-desc-price")

    # Discount
    discount = product.select_one(".product-discount")

    # Rating
    filled_stars = product.select_one(".filled-stars")

    # Reviews
    reviews = product.select_one(".rating")

    # Clean Product Name
    product_name = (
        name.get_text(strip=True)
        if name else None
    )

    # Clean Selling Price
    price_text = (
        price.get_text(strip=True)
        if price else None
    )

    if price_text:
        price_clean = re.sub(r"[^\d]", "", price_text)
        selling_price = float(price_clean) if price_clean else None
    else:
        selling_price = None

    # Clean Original Price
    original_text = (
        original_price.get_text(strip=True)
        if original_price else None
    )

    if original_text:
        original_clean = re.sub(r"[^\d]", "", original_text)
        original_price_value = (
            float(original_clean)
            if original_clean else None
        )
    else:
        original_price_value = None

    # Clean Discount
    discount_text = (
        discount.get_text(strip=True)
        if discount else None
    )

    if discount_text:
        discount_match = re.search(
            r"(\d+)",
            discount_text
        )
        discount_value = (
            float(discount_match.group(1))
            if discount_match else None
        )
    else:
        discount_value = None

    # Calculate Rating
    if filled_stars:

        style = filled_stars.get("style", "")

        rating_match = re.search(
            r"width:\s*([\d.]+)%",
            style
        )

        if rating_match:
            rating_percentage = float(
                rating_match.group(1)
            )

            rating = round(
                rating_percentage / 20,
                1
            )
        else:
            rating = None
    else:
        rating = None

    # Reviews
    if reviews:

        review_text = reviews.get_text(
            " ",
            strip=True
        )

        review_match = re.search(
            r"(\d[\d,]*)",
            review_text
        )

        if review_match:
            review_count = int(
                review_match.group(1).replace(",", "")
            )
        else:
            review_count = None

    else:
        review_count = None

    # Add data
    data.append({
        "Product_Name": product_name,
        "Selling_Price": selling_price,
        "Original_Price": original_price_value,
        "Discount_Percentage": discount_value,
        "Rating": rating,
        "Reviews": review_count
    })


# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv(
    "data/sports_shoes.csv",
    index=False
)

print("\nDataset created successfully!")

print("\nFirst 5 records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nCSV saved at:")
print("data/sports_shoes.csv")