from flask import render_template
from manage import app

@app.route('/secretaria_kim1')
def secretaria_kim1():
    return render_template('secretaria_kim/secretaria_kim-ep1.html')


