import pandas as pd
import random

categories = {
    "tshirt": ["S", "M", "L", "XL"],
    "jeans": ['28', '32', '34', '36', '38'],
    "pants": ['28', '32', '34', '36', '38'],
    "shoes": ["7", "8", "9", "10", "11", "12"],
    "watch": ["NA"],
    "bag": ['NA'],
    "hat": ["S", "M", "L", "XL"],
    "sunglasses": ["NA"]
}

brands = ["Nike", "Puma", "Reebok", "Polo", "Levis", "H&M", "Fossil", "Titan", "Wildcraft"]

colors = ["red", "blue", "black", "green", "white", "pink", "orange", "purple", "grey", "brown"]

genders = ["men", "women", "unisex"]

data = []
product_id = 1

for _ in range(250):
    category = random.choice(list(categories.keys()))
    brand = random.choice(brands)
    size = random.choice(categories[category])
    color = random.choice(colors)
    gender = random.choice(genders)

    price = random.randint(999, 4999)
    rating = round(random.uniform(3.8, 4.9), 1)
    stock = random.randint(5, 50)

    product_name = f"{brand} {category.capitalize()} {color.capitalize()}"

    data.append({
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "brand": brand,
        "size": size,
        "gender": gender,
        "price": price,
        "rating": rating,
        "stock": stock
    })

    product_id += 1

df = pd.DataFrame(data)
df.to_excel("product.xlsx", index=False)

print("Excel file created successfully ")
