# Flask-Structure-Proyect-Example
Proyecto Base para estructurar un proyecto en Flask

mi_proyecto_flask/
│
├── app/
│   ├── __init__.py              # Inicialización de la aplicación
│   ├── config.py               # Configuraciones (dev, prod, testing)
│   │
│   ├── models/                 # Modelos de datos
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── base.py            # Modelo base con métodos comunes
│   │
│   ├── views/                  # Vistas/Controladores (Blueprint)
│   │   ├── __init__.py
│   │   ├── auth.py            # Autenticación
│   │   ├── main.py            # Rutas principales
│   │   ├── api/               # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── v1/           # Versión 1 de la API
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   └── products.py
│   │   │   └── v2/           # Versión 2 de la API
│   │   │
│   │   └── admin.py           # Panel de administración
│   │
│   ├── templates/             # Plantillas Jinja2
│   │   ├── base.html         # Plantilla base
│   │   ├── layout/           # Componentes reutilizables
│   │   │   ├── header.html
│   │   │   ├── footer.html
│   │   │   └── sidebar.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── main/
│   │   │   ├── index.html
│   │   │   └── dashboard.html
│   │   └── errors/
│   │       ├── 404.html
│   │       └── 500.html
│   │
│   ├── static/               # Archivos estáticos
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   ├── auth.css
│   │   │   └── admin.css
│   │   ├── js/
│   │   │   ├── main.js
│   │   │   ├── charts.js
│   │   │   └── forms.js
│   │   ├── img/             # Imágenes
│   │   │   ├── logo.png
│   │   │   └── favicon.ico
│   │   └── uploads/         # Archivos subidos por usuarios
│   │
│   ├── services/            # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── email_service.py
│   │   └── payment_service.py
│   │
│   ├── utils/               # Utilidades/helpers
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   ├── decorators.py
│   │   ├── helpers.py
│   │   └── security.py
│   │
│   ├── forms/               # Formularios WTForms
│   │   ├── __init__.py
│   │   ├── auth_forms.py
│   │   └── product_forms.py
│   │
│   ├── extensions.py        # Extensiones de Flask inicializadas
│   └── errors.py            # Manejo de errores personalizados
│
├── migrations/              # Migraciones de base de datos (Alembic)
│   ├── versions/
│   ├── env.py
│   └── alembic.ini
│
├── tests/                  # Pruebas
│   ├── __init__.py
│   ├── conftest.py        # Configuración de pytest
│   ├── unit/
│   │   ├── test_models.py
│   │   └── test_services.py
│   ├── integration/
│   │   ├── test_auth.py
│   │   └── test_api.py
│   └── fixtures/          # Datos de prueba
│       └── test_data.py
│
├── instance/              # Configuración de instancia (no en git)
│   └── config.py         # Configuración sensible (secretos)
│
├── requirements/          # Dependencias por entorno
│   ├── base.txt          # Dependencias comunes
│   ├── dev.txt           # Desarrollo
│   ├── prod.txt          # Producción
│   └── test.txt          # Testing
│
├── scripts/              # Scripts de utilidad
│   ├── deploy.sh
│   ├── backup_db.sh
│   └── setup_env.py
│
├── .env.example          # Variables de entorno ejemplo
├── .gitignore
├── .flaskenv             # Variables para flask cli
├── docker-compose.yml    # Orquestación de contenedores
├── Dockerfile            # Configuración de Docker
├── docker-compose.prod.yml
│
├── run.py               # Punto de entrada para desarrollo
├── wsgi.py              # Punto de entrada para producción (gunicorn)
│
└── README.md            # Documentación del proyecto


===================================================================================

Estructura para API REST + Frontend:
Para API Pura (Microservicio):

api_project/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   ├── products.py
│   │   │   └── schemas.py  # Marshmallow schemas
│   │   └── v2/
│   ├── models/
│   ├── services/
│   └── utils/
├── tests/
└── requirements.txt


=====================================================================================

Para Aplicación Completa (Full-stack):

fullstack_project/
├── backend/          # Flask API
│   └── (estructura como arriba)
├── frontend/         # React/Vue/Angular
│   ├── src/
│   ├── public/
│   └── package.json
└── docker-compose.yml