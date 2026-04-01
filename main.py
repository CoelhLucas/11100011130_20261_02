from fastapi import FastAPI
app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/lucas
@app.get("/lucas")
async def lucas():
    return {"message": "Hello World01"}