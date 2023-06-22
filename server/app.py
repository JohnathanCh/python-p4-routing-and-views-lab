#!/usr/bin/env python3

from flask import Flask
import pdb

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def hello(parameter):
    print(parameter)
    return f"{parameter}"

@app.route('/count/<int:number>')
def count(number):
    # pdb.set_trace()
    return "".join([f"{num}\n" for num in range(0, number)])
    # [print(num for num in range(0, number)]
    
@app.route('/math/<int:num1>/<string:operator>/<int:num2>')
def math(num1,operator,num2):
    if operator == '+':
        return f"{num1 + num2}"
    elif operator == "-":
        return f"{num1 - num2}"
    elif operator == "*":
        return f"{num1 * num2}"
    elif operator == "div":
        return f"{num1 / num2}"
    elif operator == "%":
        return f"{num1 % num2}"
    # pdb.set_trace()

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    

