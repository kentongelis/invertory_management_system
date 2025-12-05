from flask import Blueprint, jsonify
from backend.models.data_models import *
from backend.schemas.schemas import (
    products_schema,
    suppliers_schema,
    product_suppliers_schema,
    sales_schema,
    inventory_schema,
    daily_demand_schema,
)
import time

main = Blueprint("main", __name__)


def create_db_route(route, schema, model):
    """Function that creates api route based off given handler and route name"""

    def handler():
        """Handler function that returns a database query in JSON format"""
        return jsonify(schema.dump(model.query.all()))

    endpoint_name = route.strip("/").replace("/", "_") or "root"
    main.add_url_rule(route, view_func=handler, endpoint=endpoint_name)


create_db_route("/products", products_schema, Product)
create_db_route("/suppliers", suppliers_schema, Supplier)
create_db_route("/product_suppliers", product_suppliers_schema, ProductSupplier)
create_db_route("/sales", sales_schema, Sales)
create_db_route("/inventory", inventory_schema, Inventory)
create_db_route("/daily_demand", daily_demand_schema, Daily_Demand)
