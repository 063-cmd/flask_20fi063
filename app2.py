from flask import Flask, render_template



app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index2.html')

@app.route("/rout")
def routing():
    return render_template('routing.html')


if __name__ == "__main__":
    app.run()