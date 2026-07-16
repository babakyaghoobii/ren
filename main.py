from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ سرویس روی Render به درستی کار می‌کند!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
