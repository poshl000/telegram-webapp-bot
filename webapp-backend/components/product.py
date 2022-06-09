from yaml import load, Loader

productsStream = open("config/products.yml", "r")
products = load(productsStream, Loader=Loader)

def get_product_price(product_id):
    return products[product_id]['price']

def get_delivery_price():
    return 40
