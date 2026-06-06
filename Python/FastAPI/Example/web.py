from model import Creature
from fastapi import FastAPI

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creature
    return get_creature()  # Added () to actually call the function

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app",port=8000, reload=True)