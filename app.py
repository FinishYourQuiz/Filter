from flask import Flask, request
from flask_cors import CORS
import FILTER
app = Flask(__name__)
CORS(app)

app.config['TRAP_HTTP_EXCEPTIONS'] = True

@app.route('/test', methods=['POST'])
def test():
    info = request.get_json()
    image_path = info['image']
    FILTER.filter(image_path)
        
    return "Hey"

if __name__ == '__main__':
    app.run(debug=True)