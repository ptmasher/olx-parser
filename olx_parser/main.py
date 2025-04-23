from .parser import get_page, parse_items, average_price

def main():
    query = input("Enter search query: ")
    soup = get_page(query)

    if soup:
        parse_items(soup)
        avg = average_price(query)
        print(f"Average price: {avg}")