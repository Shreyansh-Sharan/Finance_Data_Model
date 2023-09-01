from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import Backend.Utils.Data_Load_Selection as stocks_list_update

class User_input(BaseModel):
    stocks_input_payload : list

app = FastAPI()

@app.post("/fetchInformation")
async def fetchInformation(user_input:User_input):
    # print(user_input.stocks_input_payload)
    stocks_list_update.data_load_selection(user_input.stocks_input_payload)
    return {"result":user_input}

