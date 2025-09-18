import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Parameters
NUM_RECORDS = 10000
NUM_STORES = 50
NUM_PRODUCTS = 100
START_DATE = datetime(2023, 1, 1)

# Generate synthetic data
data = []
for _ in range(NUM_RECORDS):
    week_offset = random.randint(0, 51)
    date = START_DATE + timedelta(weeks=week_offset)
    store_id = random.randint(1000, 1000 + NUM_STORES)
    product_id = random.randint(5000, 5000 + NUM_PRODUCTS)
    units_sold = random.randint(1, 100)
    unit_price = round(random.uniform(5.0, 100.0), 2)
    revenue = round(units_sold * unit_price, 2)

    data.append({
        "week": date.strftime("%Y-%U"),  # Year-Week format
        "date": date.strftime("%Y-%m-%d"),
        "store_id": store_id,
        "product_id": product_id,
        "units_sold": units_sold,
        "unit_price": unit_price,
        "revenue": revenue
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("retail_sales.csv", index=False)
print("✅ retail_sales.csv generated with", NUM_RECORDS, "records.")
