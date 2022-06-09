import os
import json

from flask import Flask, Response, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, TextAreaField
from wtforms.validators import InputRequired

from prtpy.packing.improved_bin_completion import improved_bin_completion
from prtpy.bins import BinsKeepingContents

# flask setup
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class HomeForm(FlaskForm):
    submit = SubmitField('Return Home')
    download = SubmitField('DOWNLOAD')

# This form is used for the algorithms input
class DataForm(FlaskForm):
    bin_size = IntegerField("Bin Size:", validators=[InputRequired()])
    items = TextAreaField('Items csv:', validators=[InputRequired()], render_kw={'class': 'form-control', 'rows': 7})
    submit = SubmitField('Compute')


# Results page:
@app.route('/results', methods=['GET', 'POST'])
def apply():
    result = json.loads(request.args['result'])
    bin_size = request.args['bin_size']
    input_items = request.args['items']
    csv = request.args['csv']

    return render_template('result.html', form=HomeForm(), len=len(result), result=result, bin_size=f"{bin_size}" ,input_items= f"{input_items}",csv=csv)


@app.route('/download', methods=['GET', 'POST'])
def download():
    # result = json.loads(request.args['result'])
    csv = request.form['csv'] 
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                "attachment; filename=myplot.csv"})

# This function is our home page. The user should insert the input here.
@app.route('/', methods=['GET', 'POST'])
def run():
    # form for csv
    input_form = DataForm()
    form_is_valid = input_form.validate_on_submit()

    if form_is_valid:
        try:
            # get data from form
            bin_size = input_form.bin_size.data
            items_str = input_form.items.data.split(',')
            items = [int(s) for s in items_str]
            result = improved_bin_completion(BinsKeepingContents(), bin_size, items)

            csv = ''
            for i in range(result.num):
                all = result.bin_to_str(i).replace('[','').split(']')
                bins = all[0].split(',')
                for num in bins:
                    csv += num 
                    csv += ','
                csv += '\n'

            print(csv)
            # Results page:
            return redirect(url_for(apply.__name__, bin_size=bin_size, items=items.__str__(), csv=csv, result=result.bins.__str__()))
        except Exception:
            # Error page:
            return render_template('fail.html', form=HomeForm())
    else:
        return render_template('index.html', form=input_form)

if __name__ == '__main__':
    app.run(debug=True)