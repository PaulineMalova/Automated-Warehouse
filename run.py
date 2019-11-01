import os
from flask import Flask

from app.warehouse_actor import create_app

app = Flask(__name__)

config_name = os.getenv("FLASK_CONFIG")
app = create_app(config_name)


if __name__ == "__main__":
    app.run()
