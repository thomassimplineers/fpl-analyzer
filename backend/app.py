from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "Hello World! Backend fungerar korrekt"

if __name__ == '__main__':
    app.run(debug=True)
