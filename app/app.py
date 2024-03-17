from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/uploads/'
app.config['PROCESSED_FOLDER'] = 'data/processed/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['PROCESSED_FOLDER']):
    os.makedirs(app.config['PROCESSED_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return 'No file part'
    file = request.files['video']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        process_file(upload_path, filename)
        return f'<a href="/download/{filename}">Download Processed Video</a>'

def process_file(path, filename):
    output_filename = f'processed_{filename}'
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
    command = ['ffmpeg', '-i', path, '-c', 'copy', '-an', output_path]
    subprocess.run(command, check=True)
    return output_filename

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
