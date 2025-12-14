from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from app.config import config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    
    # Registrar blueprints
    from app.views.main import main_bp
    from app.views.auth import auth_bp
    from app.views.admin import admin_bp
    from app.views.api.v1 import api_v1_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')
    
    # Registrar errores personalizados
    from app.errors import register_error_handlers
    register_error_handlers(app)
    
    # Comandos CLI personalizados
    from app.commands import register_commands
    register_commands(app)
    
    return app