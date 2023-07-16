import os
import random
from MemeGenerator import MemeGenerator
from QuoteEngine import Ingestor, QuoteModel
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote"""
    if path is None:
        images_dir = os.path.join("_data", "photos", "dog")
        images = [os.path.join(images_dir, f) for f in os.listdir(images_dir)]
        path = random.choice(images)

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./temp')
    path = meme.make_meme(path, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate meme")
    parser.add_argument('--path', type=str,
                        default='./_data/photos/dog/xander_4.jpg',
                        help='path file image')
    parser.add_argument('--body', type=str, default=None, help='quote body')
    parser.add_argument('--author',
                        type=str,
                        default=None,
                        help='quote author')
    args = parser.parse_args()
    try:
        print(generate_meme(args.path, args.body, args.author))
    except Exception:
        print("Error")
