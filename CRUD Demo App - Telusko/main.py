from fastapi import FastAPI
    # lib           # class

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome Buddy"

