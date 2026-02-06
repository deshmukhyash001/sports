from flask import Blueprint

coach_bp = Blueprint("coach", __name__)

@coach_bp.route("/test")
def test_coach():
    return {"message": "Coach route working"}
