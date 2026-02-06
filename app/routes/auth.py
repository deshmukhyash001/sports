from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from ..models.models import User
from ..extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or user.password != data["password"]:
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)
    return {"token": token, "role": user.role}
