from flask import Flask, request
from flask_cors import CORS
import FILTER
app = Flask(__name__)
CORS(app)

app.config['TRAP_HTTP_EXCEPTIONS'] = True

@app.route('/getSize', methods=['POST'])
def getsize():
    info = request.get_json()
    image_path = info['image']
    return FILTER.getSize(image_path)

@app.route('/BlackAndWhite', methods=['POST'])
def black_white():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.BlackAndWhite(image_path)}

@app.route('/Reverse', methods=['POST'])
def reverse():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Reverse(image_path)}

@app.route('/Mean', methods=['POST'])
def mean():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Mean(image_path)}

@app.route('/Gaussian1', methods=['POST'])
def gaussian1():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Gaussian1(image_path)}

@app.route('/Gaussian2', methods=['POST'])
def gaussian2():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Gaussian2(image_path)}

@app.route('/Sobel1', methods=['POST'])
def sobel1():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Sobel1(image_path)}

@app.route('/Sobel2', methods=['POST'])
def sobel2():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Sobel2(image_path)}

@app.route('/Contour', methods=['POST'])
def contour():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Contour(image_path)}

@app.route('/EdgeDetection', methods=['POST'])
def edge_enhance():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.EdgeDetection(image_path)}

@app.route('/Sharpen', methods=['POST'])
def sharpen():
    info = request.get_json()
    image_path = info['image']
    return {'new_image': FILTER.Sharpen(image_path)}

@app.route('/Vintage 1', methods=['POST'])
@app.route('/Vintage 2', methods=['POST'])
@app.route('/Vintage 3', methods=['POST'])
@app.route('/Vintage 4', methods=['POST'])
@app.route('/Vintage 5', methods=['POST'])
@app.route('/Vintage 6', methods=['POST'])
def vintage():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Vintage(image_path, data)}

@app.route('/Cold 1', methods=['POST'])
@app.route('/Cold 2', methods=['POST'])
@app.route('/Cold 3', methods=['POST'])
@app.route('/Cold 4', methods=['POST'])
@app.route('/Cold 5', methods=['POST'])
@app.route('/Cold 6', methods=['POST'])
def cold():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Cold(image_path, data)}

@app.route('/Warm 1', methods=['POST'])
@app.route('/Warm 2', methods=['POST'])
@app.route('/Warm 3', methods=['POST'])
@app.route('/Warm 4', methods=['POST'])
@app.route('/Warm 5', methods=['POST'])
@app.route('/Warm 6', methods=['POST'])
def warm():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Warm(image_path, data)}

@app.route('/Winter 1', methods=['POST'])
@app.route('/Winter 2', methods=['POST'])
@app.route('/Winter 3', methods=['POST'])
@app.route('/Winter 4', methods=['POST'])
@app.route('/Winter 5', methods=['POST'])
@app.route('/Winter 6', methods=['POST'])
def winter():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Winter(image_path, data)}


@app.route('/Eq_Border1', methods=['POST'])
@app.route('/Eq_Border2', methods=['POST'])
@app.route('/Eq_Border3', methods=['POST'])
@app.route('/Eq_Border4', methods=['POST'])
@app.route('/Eq_Border5', methods=['POST'])
@app.route('/Eq_Border6', methods=['POST'])
def eq_border():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Eq_Border(image_path, data)}

@app.route('/Uneq_Border1', methods=['POST'])
@app.route('/Uneq_Border2', methods=['POST'])
@app.route('/Uneq_Border3', methods=['POST'])
@app.route('/Uneq_Border4', methods=['POST'])
@app.route('/Uneq_Border5', methods=['POST'])
@app.route('/Uneq_Border6', methods=['POST'])
def un_border():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Un_Eq_Border(image_path, data)}

@app.route('/Custom Border', methods=['POST'])
def border():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Border(image_path, data)}

@app.route('/Resize', methods=['POST'])
def resize():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Resize(image_path, int(data[0]), int(data[1]))}

@app.route('/Crop', methods=['POST'])
def crop():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Crop(image_path, int(data[0]), int(data[1]), int(data[2]), int(data[3]))}

@app.route('/Rotate', methods=['POST'])
def rotate():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Rotate(image_path, int(data))}

@app.route('/Flip Horizontal', methods=['POST'])
@app.route('/Flip Vertical', methods=['POST'])
@app.route('/Flip 90', methods=['POST'])
@app.route('/Flip 180', methods=['POST'])
@app.route('/Flip Transpose', methods=['POST'])
def filp():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Flip(image_path, int(data))}

@app.route('/Brightness1', methods=['POST'])
@app.route('/Brightness2', methods=['POST'])
@app.route('/Brightness3', methods=['POST'])
@app.route('/Brightness4', methods=['POST'])
@app.route('/Brightness5', methods=['POST'])
@app.route('/Brightness6', methods=['POST'])
def brightness():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Brightness(image_path, int(data))}

@app.route('/Contrast1', methods=['POST'])
@app.route('/Contrast2', methods=['POST'])
@app.route('/Contrast3', methods=['POST'])
@app.route('/Contrast4', methods=['POST'])
@app.route('/Contrast5', methods=['POST'])
@app.route('/Contrast6', methods=['POST'])
@app.route('/Contrast7', methods=['POST'])
def contrast():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Contrast(image_path, int(data))}

@app.route('/Sharpness1', methods=['POST'])
@app.route('/Sharpness2', methods=['POST'])
@app.route('/Sharpness3', methods=['POST'])
@app.route('/Sharpness4', methods=['POST'])
@app.route('/Sharpness5', methods=['POST'])
def sharpness():
    info = request.get_json()
    image_path, data = info['image'], info['data']
    return {'new_image': FILTER.Sharpness(image_path, int(data))}


if __name__ == '__main__':
    app.run(debug=True)