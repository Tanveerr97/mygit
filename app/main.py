from fastapi import FastAPI

app = FastAPI(title="PM2 Demo API")


@app.get("/")
def home():
    return {
        "message": "FastAPI is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Tanveer"
    }