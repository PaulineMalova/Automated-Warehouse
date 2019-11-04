from app.warehouse_actor import db


products = db.Table(
    "products",
    db.Column(
        "product_id",
        db.Integer,
        db.ForeignKey("warehouse_product.id"),
        primary_key=True,
    ),
    db.Column(
        "warehouse_id",
        db.Integer,
        db.ForeignKey("warehouse.id"),
        primary_key=True,
    ),
)


class WarehouseActor(db.Model):
    __tablename__ = "warehouse_actor"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    warehouse = db.relationship(
        "Warehouse", backref="warehouse_actor", lazy=True
    )

    def __repr__(self):
        return f"Warehouse Actor {self.first_name}"


class Warehouse(db.Model):
    __tablename__ = "warehouse"
    id = db.Column(db.Integer, primary_key=True)
    warehouse_name = db.Column(db.String(50), index=True, nullable=False)
    email = db.Column(db.String(50), index=False, nullable=False)
    warehouse_actor_id = db.Column(
        db.Integer, db.ForeignKey("warehouse_actor.id"), nullable=False
    )
    products = db.relationship(
        "Product",
        secondary=products,
        lazy="subquery",
        backref=db.backref("warehouses", lazy=True),
    )

    def __repr__(self):
        return f"Warehouse {self.warehouse_name}"


class Product(db.Model):
    __tablename__ = "warehouse_product"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    units_of_measure = db.Column(db.String(30), nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product {self.name}"

