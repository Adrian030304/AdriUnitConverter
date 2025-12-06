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

    temperature_units = {
        "Celsius":0,
        "Fahrenheit":0,
        "Kelvin":0
    }

    if request.method == 'POST':

        response_values = {k:v if v else 0 for k,v in request.form.items()}.values()

        value, _from, _to = response_values
        value = float(value)
        final = 0
        #transformam orice unitate in cea de baza celsius
        if _from.lower() == 'fahrenheit':
            final = (value - 32) * 5/9
        elif _from.lower() == 'kelvin':
            final = value - 273.15
        else:
            final = value
        
        #transformam din celsius in unitatea tinta
        if _to.lower() == 'fahrenheit':
            final = value *  9/5 + 32
        elif _to.lower() == 'kelvin':
            final = value + 273.15
        else:
            final = value

        return render_template('temperature.html', units = temperature_units, result = [value, _from, _to, final], active = 'temperature')


    return render_template('temperature.html', active='temperature', units = temperature_units)

@app.route('/weight', methods=['POST','GET'])
def weight_page():
    weight_units = {
        "miligram":pow(10,-3),
        "gram":pow(10,0),
        "kilogram":pow(10,3),
        "ounce":28.350,
        "pound":454.00
    }

    if request.method == 'POST':

        form_values = {k:float(v) if v else 0 for k,v in request.form.items()}.values()
        value, _from, _to = form_values

        f_key = next(k for k, v in weight_units.items() if v == _from)

        t_key = next(k for k, v in weight_units.items() if v == _to)

        final = value * (_from / _to)

        value, final = f"{value:.2f}", f"{final:.2f}"

        return render_template('weight.html', units = weight_units, result = [value, f_key, t_key, final], active = 'weight')

    return render_template('weight.html', active='weight', units = weight_units)