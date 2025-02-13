from flask import Flask, request, jsonify, render_template
import hashlib
import time
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

blockchain = []
genesis_block = {
    'index': 0,
    'previous_hash': '0',
    'data': 'Genesis Block',
    'timestamp': time.time(),
    'hash': 'genesis_hash'
}
blockchain.append(genesis_block)

def calculate_hash(block):
    block_string = f"{block['index']}{block['previous_hash']}{block['data']}{block['timestamp']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

@app.route('/')
def index():
    return render_template('/templates/index.html')

@app.route('/register')
def register():
    return render_template('/templates/register.html')

@app.route('/home')
def home():
    return render_template('/templates/home.html')

@app.route('/about')
def about():
    return render_template('/templates/about.html')

@app.route('/services')
def services():
    return render_template('/templates/services.html')

@app.route('/lows')
def lows():
    return render_template('/templates/lows.html')

@app.route('/adminlog')
def adminlog():
    return render_template('/templates/admin_login.html')

@app.route('/birth')
def birth():
    return render_template('/templates/user/birth.html')

@app.route('/death')
def death():
    return render_template('/templates/user/death_certificate.html')

@app.route('/id')
def id():
    return render_template('/templates/user/national_id.html')

@app.route('/marry')
def marry():
    return render_template('/templates/user/voucher.html')

@app.route('/pay')
def pay():
    return render_template('/templates/user/pay.html')

@app.route('/bir')
def bir():
    return render_template('/templates/admin/bir.html')

@app.route('/dea')
def dea():
    return render_template('/templates/admin/death.html')

@app.route('/log')
def log():
    return render_template('/templates/admin/log_sel.html')

@app.route('/p')
def p():
    return render_template('/templates/admin/pay.html')

@app.route('/select')
def select():
    return render_template('/templates/admin/selesct.html')

@app.route('/vouc')
def vouc():
    return render_template('/templates/admin/vouc.html')


@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'Data is required'}), 400
    previous_block = blockchain[-1]
    new_block = {
        'index': len(blockchain),
        'previous_hash': previous_block['hash'],
        'data': data,
        'timestamp': time.time(),
        'hash': ''
    }
    new_block['hash'] = calculate_hash(new_block)
    blockchain.append(new_block)
    return jsonify(new_block), 200

@app.route('/get_blocks', methods=['GET'])
def get_blocks():
    return jsonify(blockchain), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9899, debug=True)