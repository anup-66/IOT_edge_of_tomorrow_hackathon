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
    # text = request.form["text"]
    value = request.get_data(request)
    # value={"name":"pepsi","price":35}
    print(value)
    if len(value)==3:
        return render_template("predicted_val.html",data1=value[0][0],data2=value[0][1],data3 = value[1][0],data4 = value[1][1],total=value[2][1])
    elif len(value)==4:
        return render_template("predicted_val.html",data1=value[0][0],data2=value[0][1],data3 = value[1][0],data4 = value[1][1],data5 = value[2][0],data6 = value[2][1],total=value[3][1])
    elif len(value) == 2:
        return render_template("predicted_val.html", data1=value[0][0], data2=value[0][1],
                               total=value[1][1])
    elif len(value)==5:
        return render_template("predicted_val.html",data1=value[0][0],data2=value[0][1],data3 = value[1][0],data4 = value[1][1],data5 = value[2][0],data6 = value[2][1],data7 = value[3][0],data8 = value[3][1],total=value[4][1])
    else:
        return render_template("predicted_val.html",total = 0)

if __name__ == "__main__":
    app.run(debug=True)


