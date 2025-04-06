from fastapi import FastAPI
 
# Create a FastAPI application
app = FastAPI()
 
# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/square")
async def square(num: int):
    result = num ** 2
    return {"squared": result}