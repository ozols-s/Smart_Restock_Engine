import pandas as pd
from datetime import datetime, timedelta
import random

products = ['P001','P002','P003','P004','P005','P006','P007','P008']

def random_morning_time():
    return (
        random.randint(8, 10),
        random.randint(0, 59),
        random.randint(0, 59)
    )

stock_rows = []
date = datetime(2026,3,24)
end = datetime(2026,4,24)

# стартовые остатки (адекватные под продажи)
stock = {
    'P001': 120,
    'P002': 100,
    'P003': 140,
    'P004': 90,
    'P005': 110,
    'P006': 150,
    'P007': 130,
    'P008': 80
}

while date <= end:
    hour, minute, second = random_morning_time()
    dt = date.replace(hour=hour, minute=minute, second=second)

    for p in products:
        # расход (связан с продажами по масштабу)
        change = random.randint(-6, 3)

        # пополнение (имитирует orders)
        if random.random() < 0.25:
            change += random.randint(15, 30)

        stock[p] = max(20, stock[p] + change)

        stock_rows.append({
            "product_code": p,
            "value": stock[p],
            "date": dt.strftime('%Y-%m-%d %H:%M:%S')
        })

    date += timedelta(days=1)

pd.DataFrame(stock_rows).to_csv("dumps/stock_levels.csv", index=False)
