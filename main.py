from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/api")
def read_api_root():
    return {"Hello": "World", "Status": "Success"}

if __name__=="__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)

