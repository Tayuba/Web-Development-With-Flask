from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hom_page():
    return render_template("Ayuba.html")



if __name__ == "__main__":
    app.run(debug=True)