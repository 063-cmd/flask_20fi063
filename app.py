from flask import Flask, render_template


app = Flask(__name__)
numberList = [0,1,2,3,4,5,6,7,8,9]
dictionary = {'好きな食べ物':'寿司','好きな場所':'カフェ','好きな家具':'炭酸水メーカー'}
data = 5

@app.route("/")

def index():
    return render_template('index.html',list=numberList,dictionary=dictionary,data=data)
if __name__ == "__main__":
    app.run()