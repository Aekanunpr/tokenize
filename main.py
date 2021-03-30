import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from fastapi import FastAPI
import uvicorn

app = FastAPI()




@app.get("/cut/{text}")
def read_root(text:str):
    TEXT = text.lower()
    list_word=word_tokenize(TEXT)
    stop_words = set(stopwords.words('english'))
    filter_sentence=[word for word in list_word if not word in list(stop_words)]
    t = " ".join(filter_sentence)
    return {"text": t}
