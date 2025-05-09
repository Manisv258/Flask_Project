### Integrate HTML with Flask
### HTTP verb GET and POST


### Jinja2 template engine
"""
{% ... %}   conditional,for loops 
{{     }}   expression to print output
{# ... #}   this is for comments
"""

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

### building URL dynamically
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    exp = {'score':score,'res':res}
    return render_template('result.html',result=exp)

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

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == "POST":
        Science=float(request.form['Science'])
        Maths=float(request.form['Maths'])
        C=float(request.form['C'])
        Datascience=float(request.form['Datascience'])
        total_score = (Science+Maths+C+Datascience)/4
    res=""
    if total_score >= 50:
        res="success"
    else:
        res="fail"
    return redirect(url_for('success',score=total_score))


if __name__ == '__main__':
    app.run(debug=True)

