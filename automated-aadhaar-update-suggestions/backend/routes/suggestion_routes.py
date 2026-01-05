from flask import Blueprint, request, jsonify
from models.ml_model import generate_suggestions

suggestion_bp = Blueprint("suggestion", __name__)

@suggestion_bp.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    result = generate_suggestions(data)
    return jsonify(result)
