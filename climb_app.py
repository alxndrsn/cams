#!/usr/bin/env python
from flask import Flask, send_file, render_template, request
#import matplotlib.pyplot as plt
import StringIO, ast
import cams

app = Flask(__name__)

@app.route('/')
def main():
    return 'Text'

@app.route('/images/', methods=['GET', 'POST'])
@app.route('/images/<selected>')
def images(name=None):
    #    print selected
    all_values = request.form.listvalues()
    selected = []
    for i in all_values:
        for j in i:
            if j != 'on':
                selected.append(j) # because nested comprehensions are bad
    #selected = ",".join(selected)
    #if len selected = 0:
    return render_template('images.html', selected=selected)


@app.route('/fig/<selected>')
def chart(selected=None):
    #else:
    #results = selected.split(",")
    results = ast.literal_eval(selected)
    order_by = 2
    if len(results) == 0:
        results = None
        order_by = 0
    fig = cams.plot_data(equipment, results, order_by)
    img = StringIO.StringIO()
    #img.flush()
    fig.savefig(img, format='png', bbox_inches='tight', pad_inches=0.1)
    img.seek(0)
    #im = Image.open(img)
    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    equipment = cams.equipment
    app.run(host='0.0.0.0', debug=False)
