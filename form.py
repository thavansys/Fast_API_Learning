from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/form")
def receive_form(name: str = Form(...), password: str = Form(...)):
    return {
        "type": "Form data",
        "name": name,
        "password": password
    }