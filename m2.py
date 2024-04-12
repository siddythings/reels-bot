%%script pycodestyle
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = validate_file(file)
    if filename:
        # Save the file to disk or process it further
        file.save(os.path.join('uploads', filename))
        return redirect(url_for('show_profile', filename=filename))
    else:
        return 'Invalid file', 400