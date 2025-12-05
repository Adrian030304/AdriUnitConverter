from app import app
from flask import render_template, redirect, url_for, request, send_from_directory, send_file, Response, flash


@app.route("/")
def index():
    return redirect(url_for('length_page'))

@app.route('/length', methods=['POST','GET'])
def length_page():

    units = {
        "mm": float(pow(10,-3)),
        "cm" : float(pow(10,-2)),
        "m" :  float(pow(10,0)),
        "km": float(pow(10,3)),
        "inch": 0.0254,
        "foot": 0.0254 * 12,
        "yard": 0.0254 * 12 * 3,
        "mile": 0.0254 * 12 * 3 * 1760
    }

    result = None

    if request.method == 'POST':

        value, _from, _to = request.form.values()
        if not value:
            value = 0

        f_key = next(k for k, v in units.items() if v == float(_from))

        t_key = next(k for k, v in units.items() if v == float(_to))
        
        value, _from, _to = float(value), float(_from), float(_to)

        final = value * (_from / _to)

        value, final = f"{value:.2f}", f"{final:.2f}"
        
        return render_template('length.html', units = units, result = [value, f_key, t_key, final], active = 'length')

    return render_template('length.html', units = units, active = 'length')


@app.route('/temperature', methods=['POST','GET'])
def temperature_page():

    return render_template('temperature.html', active='temperature')

@app.route('/weight', methods=['POST','GET'])
def weight_page():

    return render_template('weight.html', active='weight')