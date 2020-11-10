import os
from flask import Flask, render_template, request, jsonify
from flask_restx import Api, Resource
from .detect import get_coordinates


def create_app(env=None):
    from app.config import config_by_name
    template_dir = os.path.abspath('./app/templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Test API", version="0.1.0")

    @app.route("/index")
    def index():
        return render_template('index.html')

    @api.route("/test")
    class Video(Resource):
        def get(self):
            return {'hello': 'world'}

        def post(self):
            uploaded_file = request.files['file']
            print(uploaded_file)
            uploaded_file.save(uploaded_file.name)
            cords = get_coordinates(uploaded_file.name)
            print(cords)
            return cords, 200

    return app
