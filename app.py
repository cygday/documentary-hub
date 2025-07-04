from flask import Flask, render_template

app = Flask(__name__)

#list of documentary yotuube video ids

video_ids = [
        "T7mTuUhhiss",
        "x9miEIklmYw",
        "0an7kovsPeQ",
        ]

@app.route('/')
def index():
    return render_template("index.html", videos=video_ids)

if __name__ == '__main__':
    app.run(debug=True)
