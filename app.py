import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Mengambil BAN_KEY dari Environment Variables Vercel/Render
BAN_KEY = os.getenv("BAN_KEY", "default_key_jika_kosong")

@app.route('/bancheck', methods=['GET'])
def bancheck():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID tidak boleh kosong!"}), 400

    try:
        # Endpoint asli dari TSun Bancheck Backend (atau disesuaikan dengan provider API TSun)
        # Jika menggunakan API backend eksternal TSun dengan autentikasi BAN_KEY:
        target_api = f"https://api.tsun-bancheck.com/check?uid={uid}&key={BAN_KEY}"
        
        response = requests.get(target_api, timeout=10)
        data = response.json()
        
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run()
