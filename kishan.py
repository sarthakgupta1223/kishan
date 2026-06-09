from flask import Flask, render_template, request, jsonify
import math
import statistics

app = Flask(__name__)

safe_dict = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "factorial": math.factorial,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "pow": pow,
    "complex": complex,
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        expression = request.json["expression"]

        result = eval(
            expression,
            {"__builtins__": None},
            safe_dict
        )

        return jsonify({"result": str(result)})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)