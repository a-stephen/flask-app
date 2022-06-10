from flask import Flask, render_template
import os
import random

app = Flask(__name__)


@app.route('/')

def get_imagesnames(path):
    for imagesdir, imagesfolder, imagesnames in os.walk(path):
        return imagesnames


def index():
    imgs = get_imagesnames("./static/images")
    random_images = random.choice(imgs)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
