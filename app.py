from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "i_am_not_feeling_sleepy_so_i_am_coding_this"
CORS(app)


@app.route('/')
def home():
    return "API is UP!<br><br>A part of @imsudip's project"


@app.route('/api/v1/gems', methods=['GET'])
def get_gems():
    from gems import get_home_page
    data = get_home_page()
    return jsonify(data)


@app.route('/api/v1/gems/<category>', methods=['GET'])
def get_category_gems(category):
    from gems import get_category_page
    data = get_category_page(category)
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
