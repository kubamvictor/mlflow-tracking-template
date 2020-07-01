from mlflow.server import app
from auth_middleware import AuthMiddleware

app.wsgi_app = AuthMiddleware(app.wsgi_app)

if __name__ == '__main__':
    app.run()
