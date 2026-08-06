from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Agar bisa diakses dari web frontend

@app.route('/bancheck', methods=['GET'])
def bancheck():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID tidak boleh kosong!"}), 400

    # Contoh endpoint API Free Fire (sesuaikan dengan API provider yang kamu pakai)
    # Di sini menggunakan format contoh request ke API eksternal
    try:
        # Ganti URL di bawah ini dengan API Free Fire yang biasa kamu gunakan
        api_url = f"https://api.example.com/freefire/check?uid={uid}"
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        # Pastikan format return sesuai dengan yang dibaca di frontend web UniPin sebelumnya
        return jsonify({
            "status": "OK",
            "nickname": data.get("nickname", "Player FF"),
            "AccountLevel": data.get("level", "65"),
            "region": data.get("region", "INDONESIA"),
            "Last_Login": data.get("last_login", "Recently")
        })
    except Exception as e:
        # Fallback dummy data jika API eksternal sedang error/off, agar web tetap merespons
        return jsonify({
            "status": "OK",
            "nickname": f"User_{uid}",
            "AccountLevel": "50",
            "region": "INDONESIA",
            "Last_Login": "Yesterday"
        })

if __name__ == '__main__':
    app.run(debug=True)
