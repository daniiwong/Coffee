import jinja2
from flask import Flask


app = Flask(__name__)

@app.route('/', method=['GET'])
def home():
    return

if __name__ == '__main__':
    app.run(debug=True)

