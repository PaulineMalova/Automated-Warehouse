from app.warehouse_actor import db


class Warehouse(db.Model):
    __tablename__ = "warehouses"
    id = db.Column(db.Integer, primary_key=True)
    warehouse_name = db.Column(db.String(50), index=True, nullable=False)
    email = db.Column(db.String(50), index=False, nullable=False)
    warehouse_actor_name = db.Column(db.String(50))

    def __repr__(self):
        return f"Warehouse {self.warehouse_name}"


class Warehouse_Actor(db.Model):
    __tablename__ = "warehouse_actors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"Warehouse Actor {self.first_name}"


class Product(db.Model):
    __tablename__ = "warehouse_products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    units_of_measure = db.Column(db.String(30), nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product {self.name}"

