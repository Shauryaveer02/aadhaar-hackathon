from flask import Flask
from flask_cors import CORS
from routes.suggestion_routes import suggestion_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

app.register_blueprint(suggestion_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Aadhaar Update Suggestion API Running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
