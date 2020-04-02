from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET']) # já é definido get como padrão do methods
def home():
    return render_template("index.html"), 200

if __name__ == "__main__":
    app.run(debug=True)