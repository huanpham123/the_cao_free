from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('b.html')  # HTML trắng nhưng tự động tải file

@app.route('/download')
def download():
    return send_from_directory('static', 'helloworld.exe', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
