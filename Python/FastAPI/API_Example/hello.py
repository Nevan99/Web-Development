from fastapi import FastAPI,Body

app = FastAPI()

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"
@app.post('/hello')
def greet(who:str = Body(embed=True)):
    return f"Hello ? {who}?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)