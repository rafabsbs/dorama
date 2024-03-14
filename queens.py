from flask import render_template
from manage import app

@app.route('/queen1')
def queen1():
    return render_template('queen/queen1.html')

@app.route('/queen2')
def queen2():
    return render_template('queen/queen2.html')