### Building Dynamic URL
### Variable Rules and URL building

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome"

### building URL dynamically
@app.route('/success/<int:score>')
def success(score):
    return f"<html><body><h1>The Result is passed with score {score}</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return f"The Person has failed and the mark is {score}"

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app.run(debug=True)

