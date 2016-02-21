from flask import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
    return render_template("search.html")

if __name__ == "__main__":
    app.run()
