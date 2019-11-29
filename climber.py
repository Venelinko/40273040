from app import main, db
from app.models import User, Article, Log

@main.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Article': Article , 'Log': Log}
