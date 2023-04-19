from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "Hello World from post router"}

@app.put("/")
async def put():
    return {"message": "Hello World from put router"}