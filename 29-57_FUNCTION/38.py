# Product information using kwargs

def product_info(**data):

    for key, value in data.items():
        print(key, ":", value)


product_info(
    name="Laptop",
    qty=5,
    price=45000,
    color="Black"
)