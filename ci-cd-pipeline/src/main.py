from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD Pipeline Running Successfully"}

@app.get("/status")
def status():
    return {"status": "healthy"}
