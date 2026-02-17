#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# index route
@app.route("/")
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter): 
    print(parameter)  
    return parameter

@app.route("/count/<int:number>")
def display_range(number):
    output = ""
    for i in range(number):
        output += f"{i}\n"
    return output

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    # Convert inputs to numbers
    n1 = int(num1)
    n2 = int(num2)
    
    if operation == '+' or operation == ' ':
        
        return str(n1 + n2)
    
    elif operation == '-':
        
        return str(n1 - n2)
    
    elif operation == '*':
        
        return str(n1 * n2)
    
    elif operation == 'div':
        
        if n2 == 0:
            return "Division by zero", 400
        return str(float(n1 / n2))
    
    elif operation == '%':
        
        return str(n1 % n2)
    
    return "Unsupported Operation", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
