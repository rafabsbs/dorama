from flask import render_template
from manage import app


@app.route('/frieren_ep22')
def frieren_ep22():
     return render_template('frieren/frieren_ep22.html')

@app.route('/frieren_ep23')
def frieren_ep23():
     return render_template('frieren/frieren_ep23.html')

@app.route('/frieren_ep24')
def frieren_ep24():
     return render_template('frieren/frieren_ep24.html')

@app.route('/frieren_ep25')
def frieren_ep25():
     return render_template('frieren/frieren_ep25.html')

@app.route('/frieren_ep26')
def frieren_ep26():
     return render_template('frieren/frieren_ep26.html')
