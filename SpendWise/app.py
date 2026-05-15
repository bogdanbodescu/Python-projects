from flask import Flask

from extensions import db
from routes import register_routes


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///spendwise.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "my_secret_key"

db.init_app(app)

register_routes(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)