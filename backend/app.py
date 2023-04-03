# -*- coding: utf-8 -*-
# @Time    : 2023/4/2 22:26
# @Author  : ddy
# @FileName: app.py
# @github  : https://github.com/ddy-ddy

from flask import Flask, request, jsonify
from flask_cors import CORS
from main import Word_kg

app = Flask(__name__)
CORS(app, supports_credentials=True)
search_engine = Word_kg()


@app.route('/search', methods=['POST','OPTIONS'])
def search():
    word = request.form.get('word')
    search_engine.search(search_word=word)
    result = search_engine.data
    # result={"word":1,"word2":2}
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5002,debug=True)
