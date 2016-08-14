#!flask/bin/python
from flask import Flask, render_template
import os, pickle

app = Flask(__name__, static_folder='static_flask', static_url_path='')

@app.route('/')
def get_tasks():
    with open('matrix.pickle', 'rb') as f:
        matrix = pickle.load(f)
    with open('words.pickle', 'rb') as f:
        words = pickle.load(f)
    with open('titles.pickle', 'rb') as f:
        titles = pickle.load(f)
    words_points = []
    for word, xy in zip(words, matrix):
        words_points.append({'word': word, 'x':xy[0], 'y':xy[1]})
    title_points = []
    for index, xy in enumerate(titles, start=1):
        title_points.append({'word': index, 'x':xy[0], 'y':xy[1]})
    return render_template("lsa.html", words = words_points, titles = title_points)

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),port=int(os.getenv("PORT", 8080)), debug=True)

#sudo pip install flask
#python run_flask_lsa.py