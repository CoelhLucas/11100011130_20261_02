import random

from fastapi import FastAPI
app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/lucas
@app.get("/randNum")
async def randnum():
    return {"Num aleatorio": random.randint(0, 1000), "Test": True}