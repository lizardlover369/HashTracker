from flask import *
app = Flask(__name__)

@app.route("/test")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.run()
