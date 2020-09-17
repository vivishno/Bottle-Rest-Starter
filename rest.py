from bottle import run, get, post, delete, request

users = [
    {
        "name": "Sai",
        "age": 34
    },
    {
        "name": "Srihan",
        "age": 4
    },
    {
        "name": "Sriven",
        "age": 7
    }
]

@get("/")
def home():
    return "Hello"

@get("/users/<name>")
def getUser(name):
    matchingUsers = [user for user in users if user['name'] == name]
    return {"user": users[0]}   

@post("/users")
def addUser():
    user = { 'name': request.json.get('name'), 'age': request.json.get('age') }
    users.append(user)
    return {"users": users}

@delete("/users/<name>")
def removeUser(name):
    matchingUsers = [user for user in users if user['name'] == name]
    users.remove(matchingUsers[0])
    return {"users": users}

@get("/users")
def getUsers():
    return {"users": users}
    
run(reloader=True, debug=True)