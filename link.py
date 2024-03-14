from flask import render_template
from manage import app


@app.route('/ep1')
def ep1():
     return render_template('link/ep1.html')

@app.route('/ep2')
def ep2():
    return render_template('link/ep2.html')

@app.route('/ep3')
def ep3():
    return render_template('link/ep3.html')

@app.route('/ep4')
def ep4():
    return render_template('link/ep4.html')

@app.route('/ep5')
def ep5():
    return render_template('link/ep5.html')

@app.route('/ep6')
def ep6():
    return render_template('link/ep6.html')

@app.route('/ep7')
def ep7():
    return render_template('link/ep7.html')

@app.route('/ep8')
def ep8():
    return render_template('link/ep8.html')