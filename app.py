from flask import Flask

# __name__ = "__main__" - Executado de forma manual
app = Flask(__name__)

@app.route("/")
def mello_world():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre"

# Excutar de forma manual - Local
if __name__ == "__main__":
    app.run(debug=True)