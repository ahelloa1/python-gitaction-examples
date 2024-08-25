from flask import Flask # type: ignore
app = Flask(__name__)

@app.route("/")

def index():
    return "Hello World 123"

if __name__ == "__main__":
    app.run()
    
