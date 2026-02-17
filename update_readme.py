from datetime import datetime
from deal_generator import generate_deals

def build_readme(deals):
    header = "# Daily Fashion & Tech Deals\n\n"
    updated = f"_Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n\n"
    intro = "Automatically generated list of current deals on fashion, tech, and luxury items.\n\n"
    body = ""

    if not deals:
        body += "No deals found today. Check back later!\n"
    else:
        for d in deals:
            body += f"- {d}\n"

    return header + updated + intro + body

if __name__ == "__main__":
    deals = generate_deals()
    content = build_readme(deals)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md updated with latest deals.")
