from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max size

@app.route('/evaluate', methods=['POST'])
def evaluate_car():
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    mileage = request.form['mileage']
    color = request.form['color']
    photos = []

    # Saving uploaded photos
    for i in range(1, 5):
        photo = request.files[f'photo{i}']
        if photo.filename == '':
            return 'No selected file', 400
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            photo.save(photo_path)
            photos.append(photo_path)
        else:
            return 'Invalid file type', 400

    # Here you would perform your evaluation logic
    # For demonstration, I'll just return the received data
    return jsonify({
        'make': make,
        'model': model,
        'year': year,
        'mileage': mileage,
        'color': color,
        'photos': photos
    })

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(debug=True)
