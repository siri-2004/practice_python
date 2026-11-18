from rc import register_customer
from sp import show_products
from atc import add_to_cart
from ct import calculate_total
from mp import make_payment



def main():
    print("=== MINI E-COMMERCE APPLICATION ===")

    customer = register_customer("Veera")
    products = show_products()

    cart = []
    cart.append(add_to_cart(products, "Laptop", 1))
    cart.append(add_to_cart(products, "Headphones", 2))

    total = calculate_total(cart)
    make_payment(customer, total)
#main()

if __name__ == "__main__":
    main()