from flask import Flask, request
from flask_cors import CORS
import FILTER
app = Flask(__name__)
CORS(app)

app.config['TRAP_HTTP_EXCEPTIONS'] = True

def temp():
    info = request.get_json()
    image_path = info['image']
    return image_path

@app.route('/BlackAndWhite', methods=['POST'])
def black_white():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.BlackAndWhite(image_path)}

@app.route('/RedEnhance', methods=['POST'])
def red_enhance():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.RedEnhance(image_path)}

@app.route('/BlueEnhance', methods=['POST'])
def blue_enhance():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.BlueEnhance(image_path)}

@app.route('/GreenEnhance', methods=['POST'])
def green_enhance():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.GreenEnhance(image_path)}

@app.route('/Reverse', methods=['POST'])
def reverse():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Reverse(image_path)}

@app.route('/OldFilm', methods=['POST'])
def old_film():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.OldFilm(image_path)}


if __name__ == '__main__':
    app.run(debug=True)