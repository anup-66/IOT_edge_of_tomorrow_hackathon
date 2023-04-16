from flask import Flask,request,render_template
from request import request
app  = Flask(__name__)


@app.route("/")

def home():
    return render_template("index.html")
wallet_money = 300
@app.route("/wallet")
def wallet():
    # wallet_money = 300
    return render_template("wallet.html",wallet_money=wallet_money)

@app.route("/userinfo")
def userinfo():
    return render_template("userinfo.html")

# @app.route("/",methods=['POST'])
# def predict():
#     # value = request.get_data()
#     return render_template("index_1.html")


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
    app.run(debug=True)