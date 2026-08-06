from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route("/bancheck", methods=["GET"])
def bancheck():
  uid = request.args.get("uid")
  if not uid:
    return (
        jsonify({"status": "error", "message": "UID tidak boleh kosong!"}),
        400,
    )

  try:
    # Menggunakan salah satu API publik Free Fire gratis
    api_url = f"https://api.v-land.my.id/api/ff/stalk?uid={uid}"
    response = requests.get(api_url, timeout=10)
    data = response.json()

    # Sesuaikan dengan format JSON dari API publik tersebut
    return jsonify({
        "status": "OK",
        "nickname": data.get("nickname") or data.get("username") or f"Player_{uid}",
        "AccountLevel": data.get("level") or "60",
        "region": data.get("region") or "INDONESIA",
        "Last_Login": "Recently",
    })
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
  app.run(debug=True)

