from fastapi import FastAPI 
from Key import Key
from llama_index import StorageContext, load_index_from_storage 
from pydantic import BaseModel 
import os   

class Question(BaseModel): 

    question: str   

app = FastAPI() 

os.environ['OPENAI_API_KEY'] =  Key
storage_context = StorageContext.from_defaults(persist_dir='./storage') 
index = load_index_from_storage(storage_context) 
query_engine = index.as_query_engine() 


@app.post("/ask") 
async def read_item(question: Question): 
    response = query_engine.query(question.question) 
    return {"response": response} 

'''@app.get("/ask") 
async def read_item(question: str): 
    response = query_engine.query(question) 
    return {"response": response}'''
 

