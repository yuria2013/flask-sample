from flask import Flask,render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    dt_now = datetime.datetime.now() + datetime.timedelta(hours=9)
    return render_template('index.html', now=dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
