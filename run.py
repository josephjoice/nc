from flask import Flask,send_file
import threading
from c import updater
app = Flask(__name__)

@app.route("/count")
def hello1():
    return str(updater.count)
@app.route("/a.js")
def hello2():
    return send_file("a.js")

@app.route("/")
def hello():
    return send_file("a.html")

if __name__ == "__main__":
    u = updater()

    t = threading.Thread(target=u.f1)
    t.start()
    app.run()
