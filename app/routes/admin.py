from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.models import User, Tournament
from ..extensions import db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/verify-tournament/<int:id>", methods=["PUT"])
@jwt_required()
def verify_tournament(id):
    admin_id = get_jwt_identity()
    admin = User.query.get(admin_id)

    if admin.role != "admin":
        return {"error": "Unauthorized"}, 403

    tournament = Tournament.query.get(id)
    tournament.is_verified = True
    db.session.commit()

    return {"message": "Tournament verified"}
