import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download the 'punkt' package if not already downloaded (required for word_tokenize)
nltk.download('punkt', quiet=True)

class Tokenizer:
    def __init__(self):
        pass

    def tokenize_words(self, text):
        word_tokens = word_tokenize(text)
        return word_tokens


    def tokenize_sentences(self, text):
        sent_tokens = sent_tokenize(text)
        return sent_tokens