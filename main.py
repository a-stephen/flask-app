from flask import Flask, render_template
import os
import random

app = Flask(__name__)

def get_imagesnames(path):
    for imagesdir, imagesfolder, imagesnames in os.walk(path):
        return imagesnames

@app.route('/')

def index():
    imgs = get_imagesnames(path="./static/images")
    random_images = random.choice(imgs)
    return render_template("index.html", mag = random_images, title="cat||dog web")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
