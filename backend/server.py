from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def root():
    return {"HUDA":"ONLINE"}

@app.get("/policy")
def policy():

    with open("../config/runtime_policy.json") as f:
        return json.load(f)
