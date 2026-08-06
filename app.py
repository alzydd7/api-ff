from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/bancheck', methods=['GET'])
def bancheck():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID tidak boleh kosong!"}), 400

    try:
        # Ganti URL di bawah ini dengan endpoint API Free Fire eksternal yang kamu gunakan
        api_url = f"https://api.example.com/freefire/check?uid={uid}"
        response = requests.get(api_url, timeout=10)
        data = response.json()
        
        # Mengembalikan data sesuai format yang dibaca oleh web UniPin dan Discord Webhook
        return jsonify({
            "status": "OK",
            "nickname": data.get("nickname", f"Player_{uid}"),
            "AccountLevel": data.get("level", "60"),
            "region": data.get("region", "INDONESIA"),
            "Last_Login": data.get("last_login", "Recently")
        })
    except Exception as e:
        # Fallback dummy data jika API eksternal sedang gangguan, 
        # supaya web dan webhook tetap sukses mengirim data
        return jsonify({
            "status": "OK",
            "nickname": f"FreeFire_{uid}",
            "AccountLevel": "65",
            "region": "INDONESIA",
            "Last_Login": "0 Year 1 Months And 5 Days Ago"
        })

if __name__ == '__main__':
    app.run(debug=True)