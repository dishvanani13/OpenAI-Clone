from flask import Flask, request, render_template
import config
from openai import OpenAI

client = OpenAI( api_key=config.API_KEY)
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{userText}"},
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    answer = response.choices[0].message.content
    return str(answer)
if __name__ == "__main__":
    app.run()