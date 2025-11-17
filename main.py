from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"Hello": "World"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"Greeting": f"Hello, {name}!"}

@app.get("/invitation-sent-to/{name}")
async def greet(name: str):
    return {"Greeting": f"we successfully sent invitation to {name}!"}