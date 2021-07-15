from flask import Flask, request
from flask_cors import CORS
import FILTER
app = Flask(__name__)
CORS(app)

app.config['TRAP_HTTP_EXCEPTIONS'] = True

@app.route('/BlackAndWhite', methods=['POST'])
def black_white():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.BlackAndWhite(image_path)}

@app.route('/RedEnhance', methods=['POST'])
def red_enhance():
    info = request.get_json()
    image_path, num = info['image'], float(info['data'])
    return {'new_image': FILTER.RedEnhance(image_path, num)}

@app.route('/BlueEnhance', methods=['POST'])
def blue_enhance():
    info = request.get_json()
    image_path, num = info['image'], float(info['data'])
    return {'new_image': FILTER.BlueEnhance(image_path, num)}

@app.route('/GreenEnhance', methods=['POST'])
def green_enhance():
    info = request.get_json()
    image_path, num = info['image'], float(info['data'])
    return {'new_image': FILTER.GreenEnhance(image_path, num)}

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

@app.route('/Blur', methods=['POST'])
def blur():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Blur(image_path)}

@app.route('/Contour', methods=['POST'])
def contour():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Contour(image_path)}

@app.route('/Detail', methods=['POST'])
def detail():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Detail(image_path)}

@app.route('/EdgeEnhance', methods=['POST'])
def edge_enhance():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.EdgeEnhance(image_path)}

@app.route('/Smooth', methods=['POST'])
def smooth():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Smooth(image_path)}

@app.route('/Sharpen', methods=['POST'])
def sharpen():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Sharpen(image_path)}

if __name__ == '__main__':
    app.run(debug=True)