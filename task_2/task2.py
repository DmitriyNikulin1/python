import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as from_file:
        data = json.load(from_file)

    with open('orders.json', 'w', encoding='utf-8') as to_file:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }

        orders_list.append(order_info)
        json.dump(data, to_file, indent=4)


if __name__ == '__main__':
    write_order_to_json('car', '7', '345345', 'Sidorov I.I.', '19.02.2021')
