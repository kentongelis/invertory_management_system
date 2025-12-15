from backend.server.extensions import db
from sqlalchemy.orm import backref


class Product(db.Model):
    """Product Model"""

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(100))
    unit_price = db.Column(db.Float)
    cost = db.Column(db.Float)
    description = db.Column(db.String(200))
    unit = db.Column(db.String(20))
    weight_kg = db.Column(db.Float)
    dimensions = db.Column(db.String(150))


class Supplier(db.Model):
    """Supplier Model"""

    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(20))


class ProductSupplier(db.Model):
    "Product and Supplier Table Model"

    __tablename__ = "product_suppliers"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))

    lead_time_days = db.Column(db.Integer)
    minimum_order_quantity = db.Column(db.Integer)
    is_primary = db.Column(db.Boolean)

    product = db.relationship("Product", backref="suppliers")
    supplier = db.relationship("Supplier", backref="products")


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
    total_amount = db.Column(db.Float)
    customer_id = db.Column(db.String(50))

    product = db.relationship("Product", backref="sales")


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    current_stock = db.Column(db.Integer)
    reorder_point = db.Column(db.Integer)
    reorder_quantity = db.Column(db.Integer)
    safety_stock = db.Column(db.Integer)
    status = db.Column(db.String(20))
    last_restocked = db.Column(db.String(50))
    warehouse_location = db.Column(db.String(50))

    product = db.relationship("Product", backref="inventory")


class Daily_Demand(db.Model):
    __tablename__ = "daily_demand"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    demand = db.Column(db.Integer)

    product = db.relationship("Product", backref="daily_demand")


class Future_Sales(db.Model):
    __tablename__ = "future_sales"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    date = db.Column(db.String(50))
    predicted_sales = db.Column(db.Float)

    product = db.relationship("Product", backref="future_sales")
