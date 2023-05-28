from flask import Flask
from routes.routes import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def home():
    return "Explore spotify tracks using python server!!!"

if __name__ == "__main__":
    app.run(debug=True) 