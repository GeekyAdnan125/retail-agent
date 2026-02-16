import pandas as pd 
import random

categories = {
    "tshirt" : ["S","M" ,"L","XL"],
    "jeans" : ['28','32','34','36','38'],
    "pants" : ['28','32','34','36','38'],
    "shoes" : ["7","8","9","10","11","12"],
    "watch" : ["NA"],
     "bag" : ['NA'],
     "hat" : ["S","M","L","Xl"],
     "sunglasses" : ["NA"]
}

brands = {
    "Nike" , "Puma" , "reebook" ,"polo","levis","H&M","fossil","titan","wildcraft"
}
color =[
    "red" ,"blue","black","green","white","pink","orange","purple","grey","brown"
]
genders = [
    "men" ,"women","unisex"
]

data = []
product_id = 1 
## loop for dummy product 
for _ in range(250):
    category = random.choice(list(categories.keys()))
    brand = random.choice(brands)
    size = random.choice(categories[category])
    color = random.choice(color)
    gender = random.choice(genders)


## price and rating 
price = random.randint(999.999)
rating = round(random.uniform((3.8,4.9),1))
stock  = random.randint(5,50)

product_name = f"{brand} {category.capitalize()}{color.capitalize()}"

data.append({
    "product_id" : product_id,
    "product_name":product_name,
    "category" : category,
    "brand" : brand,
    "size" : size,
    "gender" : gender,
    "price" : price,
    "rating" : rating,
    "stock" : stock
    })

