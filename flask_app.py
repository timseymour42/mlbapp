from flask import Flask, render_template
app = Flask(__name__)
@app.route("/news")
def news():
    return render_template('news.html')