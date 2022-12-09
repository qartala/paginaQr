from flask import Flask, send_file , render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/download')
def download_file():
    P = "app-debug.apk"
    return send_file(P, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)