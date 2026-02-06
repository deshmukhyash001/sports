from flask import Blueprint

player_bp = Blueprint("player", __name__)

@player_bp.route("/test")
def test_player():
    return {"message": "Player route working"}
