import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/answer", methods=["POST"])
def answer():
    question = request.json["question"]
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return jsonify({"answer": response.choices[0].text})

if __name__ == "__main__":
    app.run()
