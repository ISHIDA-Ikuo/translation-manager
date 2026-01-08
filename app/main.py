from fastapi import FastAPI

app = FastAPI(title="Translation Manager")

@app.get("/")
def root():
    return {"status": "ok"}
