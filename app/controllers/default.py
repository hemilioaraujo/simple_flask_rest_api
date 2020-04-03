from app import app
from flask import jsonify, request, render_template


@app.route('/', methods=['GET']) # já é definido get como padrão do methods
def home():
    return "Olá", 200
