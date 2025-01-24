from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    if 'name' in request.args.keys() and 'umur' in request.args.keys():
        name = request.args.get('name', '?')
        age = int(request.args.get('age', '?'))
        return render_template('home.html', name=name, age=age)
    elif 'name' in request.args: 
        if request.args["name"] == "budi":
            return redirect("/contact1")
        elif request.args["name"] == "santoso":
            return redirect(url_for("contact1"))
    return "404 Not Found" 

@app.route("/contact1")
def contact1():
    return "<h1>Contact Page</h1>"
    
@app.route("/tester/<string:kata>/<int:angka>/<terserah>")
def tester(kata, angka, terserah):
    return render_template('tester.html', kata=kata, angka=angka, terserah=terserah)
    
@app.route("/calc")
def calc():
    number1 = int(request.args.get('n1'))
    number2 = int(request.args.get('n2'))
    operator = request.args.get('op')
    result = number1+number2
    if operator == "+":
        result = number1+number2
    elif operator == "-":
        result = number1-number2
    elif operator == "/":
        result = number1/number2
    elif operator == "*":
        result = number1/number2
    elif operator == "%":
        result = number1%number2
    elif operator == "//":
        result = number1//number2
    elif operator == "**":
        result = number1**number2
    
    return render_template('calc.html', result=result)
     

if __name__ == '__main__':
    app.run(debug=True)