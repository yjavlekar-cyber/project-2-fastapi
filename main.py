from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Project 2 API is running",
        "features": ["Dockerized", "Jenkins-Automated"]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
