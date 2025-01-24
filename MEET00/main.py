from flask import Flask, render_template
app = Flask(__name__)

titleWeb = "FlaskKu"

data = [
    {
        'First' : '1',
        'Second' : '2',
        'Third' : '3',
    },
    {
        'First' : 'One',
        'Second' : 'Two',
        'Third' : 'Three',
    },
]

data2 = ["I", "G", "S"]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = titleWeb, data = data, usia = 20)
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/blog")
def blog():
    return render_template('blog.html')
    
@app.route("/content")
def content():
    return render_template('content.html')
    
@app.route("/igs")
def igs():
    return render_template('igs.html', data2 = data2)
     

if __name__ == '__main__':
    app.run(debug=True)
    