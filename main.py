from fastapi import FastAPI
from models import Todo

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message":"Hello World!"}

todos:list = []




# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos":todos}



# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message":"todo not found"}


# Create a Todo
@app.post("/todos")
async def create_todos(todo : Todo):
    todos.append(todo)
    return {"message":"Todo added successfully"}

# Update a  todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int, todo_obj :Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            todo.description = todo_obj.description
            return {"todo": todo}
    return {"message":"todo not found"}




# Delete todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo is Deleted Successfully"}
    return {"message":"todo not found"}