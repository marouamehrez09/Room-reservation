from flask import Flask
from routes import bp
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    app.register_blueprint(bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000)
