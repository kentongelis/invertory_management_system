from backend.server.app import app
from backend.server.extensions import db
from backend.models.data_models import (
    Product,
    Supplier,
    ProductSupplier,
    Sales,
    Inventory,
    Daily_Demand,
)
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "data"))


def load_json(filename):
    file_path = os.path.join(DATA_DIR, filename)
    with open(file_path, "r") as f:
        return json.load(f)


def load_products():
    products = load_json("products.json")
    for product in products:
        new_product = Product(
            id=product["product_id"],
            sku=product["sku"],
            name=product["name"],
            category=product["category"],
            unit_price=product["unit_price"],
            cost=product["cost"],
            description=product["description"],
            unit=product["unit"],
            weight_kg=product["weight_kg"],
            dimensions=product["dimensions"],
        )
        db.session.add(new_product)
    db.session.commit()


def load_suppliers():
    suppliers = load_json("suppliers.json")
    for supplier in suppliers:
        new_supplier = Supplier(
            id=supplier["id"],
            name=supplier["name"],
            email=supplier["email"],
            phone=supplier["phone"],
        )
        db.session.add(new_supplier)
    db.session.commit()


def load_product_suppliers():
    product_suppliers = load_json("product_suppliers.json")
    for ps in product_suppliers:
        new_ps = ProductSupplier(
            product_id=ps["product_id"],
            supplier_id=ps["supplier_id"],
            lead_time_days=ps["lead_time_days"],
            minimum_order_quantity=ps["minimum_order_quantity"],
            is_primary=ps["is_primary"],
        )
        db.session.add(new_ps)
    db.session.commit()


def load_sales():
    sales = load_json("sales.json")
    for sale in sales:
        new_sale = Sales(
            id=sale["transaction_id"],
            date=sale["date"],
            product_id=sale["product_id"],
            quantity=sale["quantity"],
            unit_price=sale["unit_price"],
            total_amount=sale["total_amount"],
            customer_id=sale["customer_id"],
        )
        db.session.add(new_sale)
    db.session.commit()


def load_inventory():
    inventory = load_json("inventory.json")
    for inv in inventory:
        new_inv = Inventory(
            product_id=inv["product_id"],
            current_stock=inv["current_stock"],
            reorder_point=inv["reorder_point"],
            reorder_quantity=inv["reorder_quantity"],
            safety_stock=inv["safety_stock"],
            status=inv["status"],
            last_restocked=inv["last_restocked"],
            warehouse_location=inv["warehouse_location"],
        )
        db.session.add(new_inv)
    db.session.commit()


def load_demand():
    demands = load_json("daily_demand.json")  # fix: was loading inventory.json
    for d in demands:
        new_demand = Daily_Demand(
            date=d["date"],
            product_id=d["product_id"],
            demand=d["demand"],
        )
        db.session.add(new_demand)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        print("Adding JSON into database...")

        load_products()
        load_suppliers()
        load_product_suppliers()
        load_sales()
        load_inventory()
        load_demand()

        print("Successfully added all JSON data.")
