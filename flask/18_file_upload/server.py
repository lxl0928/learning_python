#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/timilong/uploads'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename = filename))
    return '''
<!doctype html>
    <html>
      <head>
        <title>Upload new file</title>
      </head>
      <body>
        <h1 style="text-align: center">Upload new File</h1>
        <form action="" method=post enctype=multipart/form-data>
          <p>
            <input type=file name=file>
            <input type=submit value=Upload>
          </p>
        </form>
      </body>
    </html>
'''

if __name__ == "__main__":
    app.run(debug = True)
