from app import app
from flask import render_template, redirect, url_for, request, send_from_directory, send_file, Response, flash


@app.route("/", methods=['POST','GET'])
def index():

    units = {
        "mm": pow(10,-3),
        "cm" : pow(10,-2),
        "m" :  pow(10,0),
        "km": pow(10,3),
        "inch": 0.0254,
        "foot": 0.0254 * 12,
        "yard": 0.0254 * 12 * 3,
        "mile": 0.0254 * 12 * 3 * 1760
    }
    print(units)

    if request.method == 'POST':
        value, _from, _to = request.form.values()
        
        value, _from, _to = float(value), float(_from), float(_to)
        print(value, _from, _to)


    return render_template('index.html', units = units)


@app.route('/length')
def length_page():
    print(request.form)
