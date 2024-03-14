from flask import render_template
from manage import app


@app.route('/link_ep1')
def link_ep1():
     return render_template('link_me/link_ep1.html')

@app.route('/link_ep2')
def link_ep2():
    return render_template('link_me/link_ep2.html')

@app.route('/link_ep3')
def link_ep3():
    return render_template('link_me/link_ep3.html')

@app.route('/link_ep4')
def link_ep4():
    return render_template('link_me/link_ep4.html')

@app.route('/link_ep5')
def link_ep5():
    return render_template('link_me/link_ep5.html')

@app.route('/link_ep6')
def link_ep6():
    return render_template('link_me/link_ep6.html')

@app.route('/link_ep7')
def link_ep7():
    return render_template('link_me/link_ep7.html')

@app.route('/link_ep8')
def link_ep8():
    return render_template('link_me/link_ep8.html')