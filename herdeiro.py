from flask import render_template
from manage import app


@app.route('/herdeiro_ep1')
def herdeiro_ep1():
    return render_template('herdeiro/herdeiro-ep1.html')

@app.route('/herdeiro_ep2')
def herdeiro_ep2():
    return render_template('herdeiro/herdeiro-ep2.html')

@app.route('/herdeiro_ep3')
def herdeiro_ep3():
    return render_template('herdeiro/herdeiro-ep3.html')

@app.route('/herdeiro_ep4')
def herdeiro_ep4():
    return render_template('herdeiro/herdeiro-ep4.html')

@app.route('/herdeiro_ep5')
def herdeiro_ep5():
    return render_template('herdeiro/herdeiro-ep5.html')

@app.route('/herdeiro_ep6')
def herdeiro_ep6():
    return render_template('herdeiro/herdeiro-ep6.html')
