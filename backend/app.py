from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['video']
    if file:
        filename = secure_filename(file.filename)
        file.save(filename)
        print(filename)
        result = process_video(filename)
        return jsonify(result)
    return jsonify({'error': 'No file uploaded'})


def process_video(filename):
    # Implement video frame processing and weapon detection logic here
    # Return a result indicating if a weapon is detected or not
    weapon_detected = True  # Placeholder value, replace with actual detection result
    return {'weapon_detected': weapon_detected}


if __name__ == '__main__':
    app.run(debug=True)
