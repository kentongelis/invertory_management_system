"""
Inventory Data Generator
Generates realistic inventory data for the Inventory Management System
"""

import csv
import json
import random
from datetime import datetime, timedelta
import math

# Product categories and sample products
PRODUCTS_DATA = [
    # Electronics
    {
        "name": "Wireless Mouse",
        "category": "Electronics",
        "unit_price": 29.99,
        "cost": 15.00,
    },
    {
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "unit_price": 89.99,
        "cost": 45.00,
    },
    {
        "name": "USB-C Cable",
        "category": "Electronics",
        "unit_price": 12.99,
        "cost": 5.00,
    },
    {
        "name": "Laptop Stand",
        "category": "Electronics",
        "unit_price": 49.99,
        "cost": 20.00,
    },
    {
        "name": "Webcam HD",
        "category": "Electronics",
        "unit_price": 79.99,
        "cost": 35.00,
    },
    {
        "name": "Wireless Headphones",
        "category": "Electronics",
        "unit_price": 129.99,
        "cost": 60.00,
    },
    {
        "name": "Monitor 27 inch",
        "category": "Electronics",
        "unit_price": 299.99,
        "cost": 150.00,
    },
    {
        "name": "External SSD 1TB",
        "category": "Electronics",
        "unit_price": 119.99,
        "cost": 70.00,
    },
    # Office Supplies
    {
        "name": "Stapler Heavy Duty",
        "category": "Office Supplies",
        "unit_price": 24.99,
        "cost": 10.00,
    },
    {
        "name": "Paper Clips Box",
        "category": "Office Supplies",
        "unit_price": 4.99,
        "cost": 1.50,
    },
    {
        "name": "Printer Paper A4",
        "category": "Office Supplies",
        "unit_price": 12.99,
        "cost": 6.00,
    },
    {
        "name": "Binder Clips Assorted",
        "category": "Office Supplies",
        "unit_price": 8.99,
        "cost": 3.00,
    },
    {
        "name": "Desk Organizer",
        "category": "Office Supplies",
        "unit_price": 19.99,
        "cost": 8.00,
    },
    {
        "name": "Whiteboard Marker Set",
        "category": "Office Supplies",
        "unit_price": 14.99,
        "cost": 6.00,
    },
    {
        "name": "File Folders Pack",
        "category": "Office Supplies",
        "unit_price": 9.99,
        "cost": 4.00,
    },
    {
        "name": "Desk Lamp LED",
        "category": "Office Supplies",
        "unit_price": 34.99,
        "cost": 15.00,
    },
    # Furniture
    {
        "name": "Ergonomic Chair",
        "category": "Furniture",
        "unit_price": 299.99,
        "cost": 150.00,
    },
    {
        "name": "Standing Desk",
        "category": "Furniture",
        "unit_price": 499.99,
        "cost": 250.00,
    },
    {
        "name": "Monitor Arm",
        "category": "Furniture",
        "unit_price": 89.99,
        "cost": 40.00,
    },
    {
        "name": "Desk Mat Large",
        "category": "Furniture",
        "unit_price": 29.99,
        "cost": 12.00,
    },
    {
        "name": "Bookshelf 5-Tier",
        "category": "Furniture",
        "unit_price": 149.99,
        "cost": 75.00,
    },
    {
        "name": "Storage Cabinet",
        "category": "Furniture",
        "unit_price": 199.99,
        "cost": 100.00,
    },
    # Software & Subscriptions
    {
        "name": "Project Management License",
        "category": "Software",
        "unit_price": 99.99,
        "cost": 50.00,
    },
    {
        "name": "Cloud Storage 1TB",
        "category": "Software",
        "unit_price": 9.99,
        "cost": 5.00,
    },
    {
        "name": "Design Software License",
        "category": "Software",
        "unit_price": 199.99,
        "cost": 100.00,
    },
    # Cleaning & Maintenance
    {
        "name": "Screen Cleaner Kit",
        "category": "Maintenance",
        "unit_price": 12.99,
        "cost": 5.00,
    },
    {
        "name": "Keyboard Cleaner",
        "category": "Maintenance",
        "unit_price": 8.99,
        "cost": 3.00,
    },
    {
        "name": "Air Duster Can",
        "category": "Maintenance",
        "unit_price": 6.99,
        "cost": 2.50,
    },
]

SUPPLIERS = [
    {
        "id": 1,
        "name": "TechSupply Co.",
        "email": "contact@techsupply.com",
        "phone": "555-0101",
    },
    {
        "id": 2,
        "name": "Office Depot Pro",
        "email": "b2b@officedepot.com",
        "phone": "555-0102",
    },
    {
        "id": 3,
        "name": "Furniture Direct",
        "email": "sales@furnituredirect.com",
        "phone": "555-0103",
    },
    {
        "id": 4,
        "name": "Software Solutions Inc",
        "email": "sales@softwaresolutions.com",
        "phone": "555-0104",
    },
    {
        "id": 5,
        "name": "Maintenance Supplies Plus",
        "email": "orders@msp.com",
        "phone": "555-0105",
    },
]


def generate_products():
    """Generate products CSV with SKUs"""
    products = []
    for idx, product in enumerate(PRODUCTS_DATA, start=1):
        sku = f"{product['category'][:3].upper()}-{idx:04d}"
        products.append(
            {
                "product_id": idx,
                "sku": sku,
                "name": product["name"],
                "category": product["category"],
                "unit_price": product["unit_price"],
                "cost": product["cost"],
                "description": f"High-quality {product['name'].lower()} for professional use",
                "unit": "piece",
                "weight_kg": round(random.uniform(0.1, 15.0), 2),
                "dimensions": f"{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(5, 50)}cm",
            }
        )

    # Write CSV
    with open("products.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)

    # Write JSON
    with open("products.json", "w") as f:
        json.dump(products, f, indent=2)

    return products


def generate_suppliers():
    """Generate suppliers data"""
    # Write CSV
    with open("suppliers.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUPPLIERS[0].keys())
        writer.writeheader()
        writer.writerows(SUPPLIERS)

    # Write JSON
    with open("suppliers.json", "w") as f:
        json.dump(SUPPLIERS, f, indent=2)

    return SUPPLIERS


def generate_product_suppliers(products, suppliers):
    """Generate product-supplier relationships"""
    product_suppliers = []
    category_supplier_map = {
        "Electronics": 1,
        "Office Supplies": 2,
        "Furniture": 3,
        "Software": 4,
        "Maintenance": 5,
    }

    for product in products:
        primary_supplier = category_supplier_map.get(product["category"], 1)
        # Some products have multiple suppliers
        if random.random() > 0.7:
            supplier_ids = [
                primary_supplier,
                random.choice([s for s in suppliers if s["id"] != primary_supplier])[
                    "id"
                ],
            ]
        else:
            supplier_ids = [primary_supplier]

        for supplier_id in supplier_ids:
            product_suppliers.append(
                {
                    "product_id": product["product_id"],
                    "supplier_id": supplier_id,
                    "lead_time_days": random.randint(3, 14),
                    "minimum_order_quantity": random.choice([10, 25, 50, 100]),
                    "is_primary": supplier_id == primary_supplier,
                }
            )

    # Write CSV
    with open("product_suppliers.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=product_suppliers[0].keys())
        writer.writeheader()
        writer.writerows(product_suppliers)

    # Write JSON
    with open("product_suppliers.json", "w") as f:
        json.dump(product_suppliers, f, indent=2)

    return product_suppliers


def generate_sales_data(products, days_back=730):
    """Generate historical sales data with realistic patterns"""
    sales = []
    start_date = datetime.now() - timedelta(days=days_back)

    # Base demand patterns (some products sell more than others)
    base_demand = {}
    for product in products:
        # Electronics and office supplies tend to sell more
        if product["category"] in ["Electronics", "Office Supplies"]:
            base_demand[product["product_id"]] = random.uniform(5, 20)
        elif product["category"] == "Furniture":
            base_demand[product["product_id"]] = random.uniform(1, 5)
        else:
            base_demand[product["product_id"]] = random.uniform(2, 10)

    current_date = start_date
    transaction_id = 1

    while current_date <= datetime.now():
        # More sales on weekdays
        is_weekday = current_date.weekday() < 5
        daily_transactions = (
            random.randint(10, 50) if is_weekday else random.randint(3, 15)
        )

        # Seasonal adjustment (higher in Q4, lower in Q1)
        month = current_date.month
        if month in [11, 12]:  # Holiday season
            seasonal_multiplier = 1.5
        elif month in [1, 2]:  # Slow season
            seasonal_multiplier = 0.7
        else:
            seasonal_multiplier = 1.0

        for _ in range(daily_transactions):
            product = random.choice(products)
            product_id = product["product_id"]

            # Calculate quantity with trend and seasonality
            base_qty = base_demand[product_id]
            trend = 1 + (current_date - start_date).days / (
                days_back * 2
            )  # Slight upward trend
            quantity = max(
                1,
                int(base_qty * trend * seasonal_multiplier * random.uniform(0.5, 1.5)),
            )

            # Weekend effect
            if not is_weekday:
                quantity = max(1, int(quantity * 0.6))

            sales.append(
                {
                    "transaction_id": transaction_id,
                    "date": current_date.strftime("%Y-%m-%d"),
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": product["unit_price"],
                    "total_amount": round(quantity * product["unit_price"], 2),
                    "customer_id": f"CUST-{random.randint(1000, 9999)}",
                }
            )
            transaction_id += 1

        current_date += timedelta(days=1)

    # Write CSV
    with open("sales.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=sales[0].keys())
        writer.writeheader()
        writer.writerows(sales)

    # Write JSON (sample - first 1000 records)
    with open("sales.json", "w") as f:
        json.dump(sales[:1000], f, indent=2)

    print(f"Generated {len(sales)} sales records")
    return sales


def generate_current_inventory(products, sales):
    """Generate current inventory levels based on sales patterns"""
    inventory = []

    # Calculate average monthly sales for each product
    from collections import defaultdict

    monthly_sales = defaultdict(lambda: defaultdict(int))

    for sale in sales:
        date = datetime.strptime(sale["date"], "%Y-%m-%d")
        month_key = f"{date.year}-{date.month:02d}"
        monthly_sales[sale["product_id"]][month_key] += sale["quantity"]

    for product in products:
        product_id = product["product_id"]

        # Calculate average monthly demand
        if monthly_sales[product_id]:
            avg_monthly = sum(monthly_sales[product_id].values()) / len(
                monthly_sales[product_id]
            )
        else:
            avg_monthly = random.randint(10, 50)

        # Current stock (some products low, some high)
        current_stock = random.randint(int(avg_monthly * 0.3), int(avg_monthly * 2))

        # Reorder point (typically 1-2 months of average demand)
        reorder_point = max(10, int(avg_monthly * 1.5))

        # Reorder quantity (typically 2-3 months of demand)
        reorder_quantity = max(20, int(avg_monthly * 2.5))

        # Safety stock (typically 0.5-1 month of demand)
        safety_stock = max(5, int(avg_monthly * 0.75))

        # Stock status
        if current_stock < safety_stock:
            status = "Critical"
        elif current_stock < reorder_point:
            status = "Low"
        elif current_stock > reorder_point * 2:
            status = "Overstock"
        else:
            status = "Normal"

        inventory.append(
            {
                "product_id": product_id,
                "current_stock": current_stock,
                "reorder_point": reorder_point,
                "reorder_quantity": reorder_quantity,
                "safety_stock": safety_stock,
                "status": status,
                "last_restocked": (
                    datetime.now() - timedelta(days=random.randint(1, 60))
                ).strftime("%Y-%m-%d"),
                "warehouse_location": f"WH-{random.choice(['A', 'B', 'C'])}-{random.randint(1, 50):03d}",
            }
        )

    # Write CSV
    with open("inventory.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=inventory[0].keys())
        writer.writeheader()
        writer.writerows(inventory)

    # Write JSON
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=2)

    return inventory


def generate_daily_demand_summary(sales):
    """Generate daily demand summary for easier forecasting"""
    from collections import defaultdict

    daily_demand = defaultdict(lambda: defaultdict(int))

    for sale in sales:
        daily_demand[sale["date"]][sale["product_id"]] += sale["quantity"]

    summary = []
    for date in sorted(daily_demand.keys()):
        for product_id, quantity in daily_demand[date].items():
            summary.append({"date": date, "product_id": product_id, "demand": quantity})

    # Write CSV
    with open("daily_demand.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary[0].keys())
        writer.writeheader()
        writer.writerows(summary)

    # Write JSON (sample)
    with open("daily_demand.json", "w") as f:
        json.dump(summary[:1000], f, indent=2)

    print(f"Generated {len(summary)} daily demand records")
    return summary


if __name__ == "__main__":
    print("Generating inventory data...")

    # Change to data directory
    import os

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Generate all data
    products = generate_products()
    print(f"Generated {len(products)} products")

    suppliers = generate_suppliers()
    print(f"Generated {len(suppliers)} suppliers")

    product_suppliers = generate_product_suppliers(products, suppliers)
    print(f"Generated {len(product_suppliers)} product-supplier relationships")

    sales = generate_sales_data(products, days_back=730)  # 2 years of data

    inventory = generate_current_inventory(products, sales)
    print(f"Generated inventory levels for {len(inventory)} products")

    daily_demand = generate_daily_demand_summary(sales)

    print("\n✅ All data files generated successfully!")
    print("\nGenerated files:")
    print("  - products.csv / products.json")
    print("  - suppliers.csv / suppliers.json")
    print("  - product_suppliers.csv / product_suppliers.json")
    print("  - sales.csv / sales.json")
    print("  - inventory.csv / inventory.json")
    print("  - daily_demand.csv / daily_demand.json")
