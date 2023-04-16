from flask import Flask,request,render_template
from request import request
app  = Flask(__name__)


@app.route("/")

def home():
    return render_template("index.html")

# @app.route("/",methods=['POST'])
# def predict():
#     # value = request.get_data()
#     return render_template("index.html")


@app.route("/predicted_val", methods=["POST"])
def display_text():
    values = request.get_data(request)
    print(values)
    totals = {}
    for value in values:
        name = value['name']
        price = int(value['price'])
        if name in totals:
            totals[name] += price
        else:
            totals[name] = price

    List = [{'name': name, 'price': price} for name, price in totals.items()]
    print(List)

    total = 0

    for value in values:
        if 'price' in value:
            total = total + value['price']
    return render_template("predicted_val.html",values = List,total = total)

if __name__ == "__main__":
    app.run(host = '192.168.237.81',port=5000,debug=True)


