from marshmallow import Schema, fields


class WarehouseActorSchema(Schema):
    id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    middle_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    warehouse = fields.Nested('WarehouseSchema', dump_only=True, only="warehouse_name")


class WarehouseSchema(Schema):
    id = fields.Int(required=True)
    warehouse_name = fields.Str(required=True)
    email = fields.Str(required=True)
    warehouse_actor_id = fields.Str(
        dump_only=True, 
        required=True, 
        error_messages={"required":"Warehouse actor id required"})
    products = fields.Nested(
        "ProductSchema", many=True, dump_only=True, exclude="warehouse"
    )    


class ProductSchema(Schema):
    id = fields.Int(required=True)
    product_name = fields.Str(required=True)
    units_of_measure = fields.Str(required=True)
    unit_price = fields.Int(required=True)
 