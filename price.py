def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
fp = format_price(56.24)
print(fp)