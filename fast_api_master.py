from fastapi import FastAPI
from pydantic import BaseModel

class User_input(BaseModel):
    x : []

app = FastAPI()

@app.post("/fetch")
def data_load_selection(input:User_input):
    result = data_load_selection(input.x)
    return result