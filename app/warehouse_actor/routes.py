# from flask import request, render_template, make_response
# from flask import current_app as app
# from .models import db, Products, Warehouse


# @app.route('/', methods=['GET'])
# def create_warehouse():
#     """Create a warehouse"""
#     warehouse_name = request.args.get('warehouse_name')
#     email = request.args.get('email')
#     if warehouse_name and email:
#         existing_warehouse = User.query.filter(Warehouse.warehouse_name == warehouse_name or Warehouse.email == email).first()
#         if existing:
#             return make_response(f'{warehouse_name} ({email}) already created!')

#         new_warehouse = Warehouse(warehouse_name = warehouse_name,
#                                  email = email,
#                                  )    
#         db.session.add(new_warehouse)
#         db.session.commit()

#     return make_response(f"{new_warehouse} successfully created!")                             