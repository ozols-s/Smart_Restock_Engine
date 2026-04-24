import pandas as pd
from datetime import datetime, timedelta
import random

products = ['P001','P002','P003','P004','P005','P006','P007','P008']
clients = ['C001','C002','C003']

# цены из orders (фиксированные базы)
base_prices = {
    'P001': 1200,
    'P002': 110,
    'P003': 95,
    'P004': 300,
    'P005': 150,
    'P006': 75,
    'P007': 85,
    'P008': 500
}

def random_time():
    return (
        random.randint(8, 23),
        random.randint(0, 59),
        random.randint(0, 59)
    )

sales_rows = []
date = datetime(2026,1,23)
end = datetime(2026,4,24)

id_counter = 1

while date <= end:
    for _ in range(random.randint(3,4)):
        product = random.choice(products)
        quantity = random.randint(250, 300)

        # ✔ правильный шум — через цену
        price = base_prices[product] * random.uniform(0.97, 1.03)

        hour, minute, second = random_time()
        dt = date.replace(hour=hour, minute=minute, second=second)

        revenue = quantity * price

        sales_rows.append({
            "id": id_counter,
            "product_code": product,
            "client_code": random.choice(clients),
            "revenue": round(revenue, 2),
            "quantity": quantity,
            "date": dt.strftime('%Y-%m-%d %H:%M:%S')
        })

        id_counter += 1

    date += timedelta(days=1)

pd.DataFrame(sales_rows).to_csv("dumps/sales.csv", index=False)
