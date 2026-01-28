from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    print("IP:", ip)

    return redirect("https://www.deepseek.com/en/")  # ← сюда меняешь ссылку

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
