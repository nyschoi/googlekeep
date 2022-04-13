from flask import Flask

app = Flask(__name__)  # app
# print(app.config['DEBUG'])


@app.route('/')
def index():
    return 'hello flask!!!'


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='localhost')
