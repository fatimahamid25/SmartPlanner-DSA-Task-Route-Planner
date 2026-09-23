from flask import Flask, render_template

app = Flask(__name__, static_folder="frontend", static_url_path="/frontend")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/dependencies")
def dependencies():
    return render_template("dependencies.html")


@app.route("/routes")
def routes():
    return render_template("routes.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


if __name__ == "__main__":
    app.run(debug=True)