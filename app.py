from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<p>this is product page</p>"

if __name__ == "__main__":
    app.run(debug=True , port = 8000)  # debug=true helps to give error in browser, default port 5000
