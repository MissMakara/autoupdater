from flask import Flask
from flask_restful import Api
from views.main import main
from views.updater import Updater

app = Flask(__name__)
api = Api(app)

#endpoints
app.add_url_rule("/", view_func=main)
api.add_resource(Updater, "/update")

if __name__=="__main__":
    app.run(port = 5000, debug=True)
