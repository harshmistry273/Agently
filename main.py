import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", "0.0.0.0",port=8000)