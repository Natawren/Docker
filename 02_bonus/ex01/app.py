from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'If you see it, that means, that she wrote a simple Flask app. It is really wonderfull, do not forget to give a point. Better - 2 points :)'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')