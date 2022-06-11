from flask import Flask, render_template
import os
import random

app = Flask(__name__)

def get_imagesnames(path):
    for imagesdir, imagesfolder, imagesnames in os.walk(path):
        return imagesnames

@app.route('/')

def index():
    path="./static/images/"
    imgs = get_imagesnames(path)
    random_images = random.choice(imgs)
    img_path = path+random_images
    return render_template("index.html", mg = img_path, title="cat||dog-web")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
