from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField
import os
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretekey'
app.config['UPLOAD_FOLDER'] = 'static/files/'

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[FileRequired()])
    submit = SubmitField('Upload File')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return f'File {filename} uploaded successfully!'
    
    return render_template('index.html', form=form)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("running")
    app.run(debug=True)

