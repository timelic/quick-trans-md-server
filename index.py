from flask import Flask, request

from translate import translate

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "OPTIONS"])
def main():
    request_json = request.get_json(force=True)
    text = request_json.get("text")
    lang = request_json.get("lang")
    lang = "ja" if lang == "jp" else lang
    res = translate(text, lang)
    print(res)
    headers = {
        "Content-Type": "text/plain",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST",
    }
    return res, 200, headers


app.run(port=8080)
