from fastapi import FastAPI
import uvicorn

app = FastAPI()




@app.get("/cut")
def read_root(text:str):
    TEXT = text.lower()
    list_word=TEXT.split()
    #stop_words = set(stopwords.words('english'))
    #filter_sentence=[word for word in list_word if not word in list(stop_words)]
    return {"text": str(list_word)}#filter_sentence}
