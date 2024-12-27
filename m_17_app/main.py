from fastapi import FastAPI
from routers import task
from routers import user
app = FastAPI()

@app.get('/')
async def mess_dict():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)


#   uvicorn main:app --reload
#   http://127.0.0.1:8000
#   http://127.0.0.1:8000/docs