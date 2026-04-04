from flask import Flask
import config

client = OpenAI( api_key=config.API_KEY)
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()