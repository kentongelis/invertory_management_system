from backend.server.extensions import db
from backend.models.data_models import (
    Product,
    Supplier,
    ProductSupplier,
    Sales,
    Inventory,
    Daily_Demand,
    Future_Sales,
)
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Function to create schema for each model


def create_schema(given_model):
    class GenericSchema(SQLAlchemyAutoSchema):
        class Meta:
            model = given_model
            sqla_session = db.session
            load_instance = True
            ordered = True
            include_fk = True

    return GenericSchema


# Establish all schemas

ProductSchema = create_schema(Product)
SupplierSchema = create_schema(Supplier)
ProductSupplierSchema = create_schema(ProductSupplier)
SalesSchema = create_schema(Sales)
InventorySchema = create_schema(Inventory)
DailyDemandSchema = create_schema(Daily_Demand)
FutureSalesSchema = create_schema(Future_Sales)

# Create lists of database instances

products_schema = ProductSchema(many=True)
suppliers_schema = SupplierSchema(many=True)
product_suppliers_schema = ProductSupplierSchema(many=True)
sales_schema = SalesSchema(many=True)
inventory_schema = InventorySchema(many=True)
daily_demand_schema = DailyDemandSchema(many=True)
future_sales_schema = FutureSalesSchema(many=True)
