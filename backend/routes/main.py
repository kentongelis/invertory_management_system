from flask import Blueprint, Response, request, jsonify
import json
from backend.models.data_models import *
from backend.schemas.schemas import (
    products_schema,
    suppliers_schema,
    product_suppliers_schema,
    sales_schema,
    inventory_schema,
    daily_demand_schema,
    future_sales_schema,
)
from backend.langchain.langchain import get_langchain_answer

main = Blueprint("main", __name__)


@main.route("/ask_db", methods=["POST"])
def ask_db():
    question = request.form.get("question")
    result = get_langchain_answer(question)
    return jsonify({"result": result})


def create_db_route(route, schema, model):
    def handler():
        data = schema.dump(model.query.all())
        return Response(
            json.dumps(data, ensure_ascii=False, sort_keys=False),
            mimetype="application/json",
        )

    endpoint_name = route.strip("/").replace("/", "_") or "root"
    main.add_url_rule(route, view_func=handler, endpoint=endpoint_name)


create_db_route("/products", products_schema, Product)
create_db_route("/suppliers", suppliers_schema, Supplier)
create_db_route("/product_suppliers", product_suppliers_schema, ProductSupplier)
create_db_route("/sales", sales_schema, Sales)
create_db_route("/inventory", inventory_schema, Inventory)
create_db_route("/daily_demand", daily_demand_schema, Daily_Demand)
create_db_route("/future_sales", future_sales_schema, Future_Sales)
