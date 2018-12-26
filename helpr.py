from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    test = [
        {
            'first': 'Tim',
            'last': 'Grob'
        }
    ]
    return test


if __name__ == '__main__':
    app.run(debug=True)
