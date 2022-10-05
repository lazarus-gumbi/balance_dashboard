from tabnanny import check
import time
from urllib import response
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/get_balances",methods=['GET','POST'])
def get_balance():
    try:
        float_balance = 123.23
        check_balance = 320.23
        time.sleep(2)
        return jsonify(
            {
                "status": "success",
                "balances": {"float": float_balance, "check": check_balance},
            }
        )
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"})


if __name__ == "__main__":
    app.run(debug=True)
