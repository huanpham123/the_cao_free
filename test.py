from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('b.html')

@app.route('/download')
def download_file():
    # Đường dẫn đến file .exe trong thư mục static
    return send_from_directory('static', 'helloworld.zip', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
