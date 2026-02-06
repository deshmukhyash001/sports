from flask import Blueprint

public_bp = Blueprint("public", __name__)

@public_bp.route("/test")
def test_public():
    return {"message": "Public route working"}
