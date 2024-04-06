from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField
import os
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretekey'
ALLOWED_EXTENSIONS = {'jpg', 'pdf'}
dir_path = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(dir_path, "statics")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[FileRequired()])
    submit = SubmitField('Upload File')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            return render_template('result.html', pill_name = "fish oil")
    
    return render_template('index.html', form=form)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("running")
    app.run(debug=True)

