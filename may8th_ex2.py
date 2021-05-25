'''creating a login form using flask displaying success on submitting using JavaScript'''


from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/successjs", methods = ['POST', "GET"])
def successjs():
    if request.method == 'POST':
        result = request.form
        return render_template("success_js.html", result= result)


if __name__ == '__main__':
    app.run(debug=True)