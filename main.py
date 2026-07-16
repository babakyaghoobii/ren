from flask import Flask, request
import os

app = Flask(__name__)

UUID = "b831d6b5-7b3a-4a6f-9c2e-8f1a5d9e7c3b"

@app.route('/')
def index():
    host = request.headers.get('Host', 'localhost')
    link = f"vless://{UUID}@{host}:443?security=tls&sni=www.aparat.com&type=ws&host=www.aparat.com&path=/&flow=xtls-rprx-vision#Iran-Config"
    return f"""
    <html><body style="text-align:center;padding:40px;font-family:sans-serif;background:#f0f0f0">
        <h1 style="color:#dc2626">✅ کانفیگ VLESS آماده است</h1>
        <div style="background:#fff;padding:20px;border-radius:12px;word-break:break-all;max-width:700px;margin:20px auto;border:1px solid #ddd">
            <code>{link}</code>
        </div>
        <p>لینک رو کپی کن و توی V2rayNG وارد کن.</p>
    </body></html>
    """

@app.route('/sub')
def subscribe():
    host = request.headers.get('Host', 'localhost')
    link = f"vless://{UUID}@{host}:443?security=tls&sni=www.aparat.com&type=ws&host=www.aparat.com&path=/&flow=xtls-rprx-vision#Iran-Config"
    return link

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
