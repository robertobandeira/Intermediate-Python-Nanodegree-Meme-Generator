"""Runs backend server through flask and handles calls to meme."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel
import shutil

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for infile in quote_files:
        temp_quotes = Ingestor.parse(infile)
        for quote in temp_quotes:
            quotes.append(quote)

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    temp_img = f'./tmp/{random.randint(0,1000000)}.jpeg'
    image_url = request.form['image_url']
    try:
        res = requests.get(image_url, stream=True)
        if res.status_code == 200:
            with open(temp_img, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
        body = request.form['body']
        author = request.form['author']
        path = meme.make_meme(temp_img, body, author)
        os.remove(temp_img)
    except Exception:
        print("Image couldn't be fetched. Please try a different url")
        return render_template('meme_error.html')
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
