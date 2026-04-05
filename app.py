from flask import Flask, request, render_template
import config
from openai import OpenAI

client = OpenAI( api_key=config.API_KEY)
app = Flask(__name__)
conversation_history = []
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    model_engine = "gpt-3.5-turbo"
    conversation_history.append({'role': 'user', 'content': userText})
    response = client.chat.completions.create(
        
        model=model_engine,
        messages= conversation_history,

        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    ai_responce = response.choices[0].message.content
    return str(ai_responce)
if __name__ == "__main__":
    app.run()