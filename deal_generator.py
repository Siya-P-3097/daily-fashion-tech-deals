import random

products = [
    {
        "name": "Lululemon Align Leggings",
        "price": 89.00,
        "target": 95.00,
        "link": "https://www.example.com/lululemon?aff=YOURTAG"
    },
    {
        "name": "Dyson V11 Vacuum",
        "price": 499.00,
        "target": 550.00,
        "link": "https://www.example.com/dyson?aff=YOURTAG"
    },
    {
        "name": "Alo Yoga Hoodie",
        "price": 98.00,
        "target": 110.00,
        "link": "https://www.example.com/aloyoga?aff=YOURTAG"
    }
]

templates = [
    "🔥 Deal Alert: {name} is now ${price}! {link}",
    "💸 Price Drop: {name} is on sale for ${price}. {link}",
    "✨ Trending Deal: {name} just dropped in price — now ${price}. {link}",
    "🛍️ Fashion Steal: {name} is discounted to ${price}. Grab it here: {link}"
]

def generate_deals():
    messages = []
    for p in products:
        if p["price"] <= p["target"]:
            msg = random.choice(templates).format(**p)
            messages.append(msg)
    return messages
