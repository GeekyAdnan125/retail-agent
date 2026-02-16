import pandas as pd
import re
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

## load the product data
df = pd.read_excel("data\product.xlsx")
df = df.fillna(" ")

## llm setup
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant"
)


def recoment_product(user_input: str, user_name: str | None = None):

    query = user_input.lower().strip()

    # Greeting
    if query in ["hi","hii","hey","hello","hellow"]:
        return f"Hello {user_name or ''}! How can I assist you in filtering the perfect product today?"

    filtered_df = df.copy()

    # Category filter
    if "shoes" in query or "shoe" in query:
        filtered_df = filtered_df[filtered_df['category'].str.lower() == 'shoes']

    if "tshirt" in query or "t-shirt" in query:
        filtered_df = filtered_df[filtered_df['category'].str.lower() == 'tshirt']

    if "bag" in query or "bags" in query:
        filtered_df = filtered_df[filtered_df['category'].str.lower() == 'bag']

    if "sunglasses" in query or "sunglass" in query:
        filtered_df = filtered_df[filtered_df['category'].str.lower() == 'sunglasses']

    if "hat" in query or "hats" in query:
        filtered_df = filtered_df[filtered_df['category'].str.lower() == 'hat']

    if "jean" in query or "jeans" in query:
        filtered_df = filtered_df[filtered_df['category'].str.lower() == 'jeans']

    # Color filter
    for color in ["red","blue","black","green","white","pink","orange","purple","grey","brown"]:
        if color in query:
            filtered_df = filtered_df[filtered_df['color'].str.lower() == color]
            break

    # Price filter
    price_match = re.search(r"(under|below|less than)\s*(\d+)", query)
    if price_match:
        max_price = int(price_match.group(2))
        filtered_df = filtered_df[filtered_df["price"] <= max_price]

    # If nothing found
    if filtered_df.empty:
        return (
            "Thank you for your query. At the moment, we don't have products that exactly match your requirement.\n"
            "Would you like me to check similar options?"
        )

    # Prepare product list
    product_text = ""
    for _, row in filtered_df.head(5).iterrows():
        product_text += (
            f"{row['product_name']} | {row['brand']} | ₹{row['price']} | {row['color']} | {row['size']}\n"
        )

    greeting = f"Hello {user_name}," if user_name else "Hello"

    prompt = f"""
You are a professional e-commerce shopping assistant.

{greeting}

Customer request:
{user_input}

Here are the best matching products:
{product_text}

Respond in a friendly and helpful way.
"""

    response = llm.invoke(prompt)

    return response.content

q = input("Enter you q")
print(recoment_product(q))
