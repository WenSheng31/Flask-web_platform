from app import db
from sqlalchemy.exc import SQLAlchemyError

def check_db_connection():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return True
    except SQLAlchemyError:
        return False
