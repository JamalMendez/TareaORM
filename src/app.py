from flask import Flask
from config import DevelopmentConfig  # Import the 'DevelopmentConfig' class from the config module

#rutas
from routes import helados


app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not Found Page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(DevelopmentConfig)  # Access the 'development' configuration

    #Blueprints
    app.register_blueprint(helados.main, url_prefix='/api/helados')

    app.register_error_handler(404, page_not_found)
    app.run()
